
# 분산락

> 왜 분산락을 적용하는가?

동일한 Merge Request(이하 MR)에 대해 **동시에 여러 개의 Webhook 이벤트가 들어오더라도, AI 리뷰는 딱 1번만** 실행되도록 보장하기 위해.

> 어떻게 구현했는가?

- 일반적인 Redis `SETNX`(Set if Not eXists)는 구현이 복잡하고(락 획득 재시도 로직 등) 해제 과정에서 원자성 문제가 발생할 수 있음.
- **Redisson**은 이런 복잡한 Redis 기반 분산락을 자바의 `Lock` 인터페이스처럼 아주 쉽고 안전하게 쓸 수 있게 해주는 라이브러리라서 이를 채용.

## 1
```java
@Async
public void review(Long projectId, Long mrIid, String mrTitle) {
```
- **비동기 시작:** Webhook 컨트롤러가 이벤트를 받자마자 이 메서드를 던져놓고 200 OK를 반환.
- 이 메서드는 톰캣 스레드가 아닌 별개의 백그라운드 스레드(`task-1`, `task-2` 등)에서 실행됨.

## 2
```java
    // 락(Lock)의 이름(Key) 생성
    String lockKey = "mr_review:" + projectId + ":" + mrIid;
    RLock lock = redissonClient.getLock(lockKey);
```
- **락 키(Lock Key) 정의:** 락의 이름을 `mr_review:프로젝트ID:MR번호`로 지정
	- 예: `mr_review:1284647:13`
- 여러 스레드가 동시에 실행되더라도, **같은 MR 번호(13번)에 대해서는 오직 하나의 스레드만 이 락(Key)을 점유할 수 있음.** (만약 MR 14번 이벤트가 들어오면 키가 다르므로 락 점유 경쟁을 하지 않고 바로 실행됩니다.)

## 3
```java
boolean acquired = false;
    try {
        // 락 획득 시도 (획득 대기시간: 0초 / 락 만료시간: 300초(5분))
        acquired = lock.tryLock(0, 300, TimeUnit.SECONDS);
```
- **락 획득 시도 (`tryLock`)**
- **대기시간(`waitTime`) 0초:** 누군가 이미 이 MR 번호로 락을 잡고 있다면, 기다리지 않고 즉시 포기. (동일 이벤트 중복 실행을 막는 핵심)
- **만료시간(`leaseTime`) 300초:** 락을 획득한 스레드가 AI 호출 도중 서버가 멈추거나 에러가 나서 락을 해제(unlock)하지 못하는 최악의 버그(데드락)에 빠지더라도, Redis가 5분 뒤에 락을 강제로 삭제해서 다음 번에는 정상 동작하도록 풀어줌.

## 4
```java
if (!acquired) {
            // 락을 얻지 못함 = 누군가 이미 이 MR번호로 리뷰를 진행 중임!
            log.info("[MR Review] 이미 처리 중: project={}, mr={}", projectId, mrIid);
            return; // 아무것도 안 하고 그냥 종료. (방어 성공)
        }
```
- **획득 실패 시 차단:** 락을 못 얻었으면(누군가 이미 실행 중이면) 뒤도 안 돌아보고 메서드를 종료(`return`).
	- 여기서 중복 실행이 차단되는 것.

## 5
```java
log.info("[MR Review] 시작: project={}, mr={}", projectId, mrIid);
        // --- 락이 걸려있는 안전지대 (독점 실행 구간) ---
        String diff = fetchDiff(projectId, mrIid);       // GitLab에서 코드 가져오기
        String review = requestReview(diff, mrTitle);    // AI한테 넘기고 2~30초 대기
        postComment(projectId, mrIid, review);           // GitLab에 댓글 달기
        // ---------------------------------------------
```
- **안전지대 (Critical Section):** 락을 획득한 딱 하나의 스레드만 이 구간에 진입함.
- AI 응답이 30초가 걸리든 1분이 걸리든, 이 스레드가 이 구간을 빠져나가 락을 풀기 전까지는 같은 MR 번호로 들어온 다른 이벤트들은 앞선 단계에서 튕겨 나감.

## 6
```java
} catch (Exception e) {
        log.error("[MR Review] 오류: project={}, mr={}, error={}", projectId, mrIid, e.getMessage(), e);
    } finally {
        if (acquired && lock.isHeldByCurrentThread()) {
            lock.unlock();
        }
    }
}
```
- **락 해제 보장 (`finally`):**
	- 일이 무사히 끝났든, 중간에 예외(`Exception`)가 터져서 망했든 상관없이 **`finally` 구문은 무조건 실행됨**
- `lock.isHeldByCurrentThread()`: 내가 진짜로 이 락의 주인이 맞는지 한 번 더 안전하게 확인하는 로직.
- `lock.unlock()`: Redis에서 해당 락(Key)을 삭제하여, 비로소 다음번 동일 MR 이벤트가 실행될 수 있게 자리를 비워줌.

# 결과

## 분산락
![[Pasted image 20260306214221.png]]

```
[Webhook] MR 이벤트 수신: project=1284647, mr=14, action=open
[MR Review] 시작: project=1284647, mr=14

[Webhook] MR 이벤트 수신: project=1284647, mr=14, action=open
[MR Review] 이미 처리 중: project=1284647, mr=14
```
- 같은 `Merge Request id`에 대해서 이미 처리 중이라는 로그가 찍히는 것을 확인 가능.
- 즉, 하나의 `MR`이 열려서 특정 스레드가 락을 점유하면 그 이후에 오는 동일한 `MR`에 대한 리뷰는 중단되게 됨.

## 그런데...
사실상 의미 없는 작업이기는 함. 그래도 레디스 분산락을 체험해볼겸 진행해봄.

