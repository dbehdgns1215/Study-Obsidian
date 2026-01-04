

# 트랜잭션 · 락 · Saga 핵심 정리 (실무 기준)

## 1. 트랜잭션 기본 개념
- 트랜잭션 = “이 범위 안의 작업은 전부 성공 or 전부 실패”
- Spring 기준: `@Transactional` 메서드 단위
- 롤백 기준: **unchecked exception(RuntimeException)**

---

## 2. SELECT FOR UPDATE (비관적 락)

### 개념
```sql
SELECT * FROM account WHERE id = ? FOR UPDATE;
```

SELECT 시점에 row-level write lock

트랜잭션 종료(COMMIT/ROLLBACK)까지 유지

다른 트랜잭션:

같은 row FOR UPDATE → 대기

UPDATE / DELETE → 대기

언제 쓰나

돈

재고

좌석

쿠폰

👉 “동시 수정 절대 허용 안 되는 데이터”

---

## 3. 비관적 락 vs 낙관적 락

### 비관적 락

- “충돌 날 거라 가정하고 미리 잠금”
    
- 장점: 안정성
    
- 단점: 대기, 성능 저하
    
- 대표 수단: SELECT FOR UPDATE
    

### 낙관적 락

- “충돌 나면 그때 실패 처리”
    
- 구현: @Version
    
- UPDATE 시 version 비교
    
- 충돌 시 OptimisticLockException
    

```java
@Version
private Long version;
```

---

## 4. 낙관적 락 + 자동 재시도 (@Retryable)

### 중요한 전제

- idempotent 작업만 가능
    
- 다시 실행해도 결과가 같아야 함
    

### 가능한 예

- 설정 저장
    
- 프로필 수정
    
- 조회수 증가
    

### 불가능한 예

- 출금
    
- 결제
    
- 포인트 차감
    

### 내부 동작 핵심

- 재시도 = 메서드 전체 재실행
    
- 매번 DB에서 다시 조회
    
- 최신 version은 JPA가 자동 반영
    
- 개발자가 version 직접 관리 ❌
    

---

## 5. 트랜잭션에서 자주 터지는 실수

### 1) 예외 삼킴

```java
try {
    ...
} catch (Exception e) {
    // 로그만 찍음
}
```

→ 롤백 안 됨

### 2) 같은 클래스 내부 호출

```java
this.method(); // @Transactional 안 먹음
```

### 3) 외부 API를 트랜잭션 안에 둠

DB 락 장시간 유지

장애 유발

---

## 6. 외부 API + DB 작업의 정답 구조

- DB 트랜잭션은 짧게
    
- 외부 호출은 트랜잭션 밖에서
    

→ 그래서 Saga 패턴

---

## 7. Saga 개념 (현실 버전)

### 한 줄 정의

“단일 트랜잭션을 포기하고  
상태 + 단계별 실행 + 보상으로 처리”

### 핵심 요소

- 상태 테이블
    
- 단계별 트랜잭션
    
- 실패 시 보상 트랜잭션
    

---

## 8. Saga 상태 테이블 예시

```
TRANSFER
-------------------------
id
from_account_id
to_account_id
amount
status
```

status 흐름:

```
INIT
 → WITHDRAWN
 → COMPLETED
```

실패 시:

```
WITHDRAWN → CANCELED
```

---

## 9. Saga 실행 흐름 (계좌이체)

1. Controller
    

- Saga 시작만 요청
    

2. 출금 단계 (TX)
    

- 비관적 락
    
- 잔액 차감
    
- status = WITHDRAWN
    

3. 외부 작업
    

- 트랜잭션 ❌
    
- 오래 걸려도 OK
    

4. 성공 시
    

- 입금 (TX)
    
- status = COMPLETED
    

5. 실패 시
    

- 출금 보상 (TX)
    
- status = CANCELED
    

---

## 10. Spring 이벤트의 정체

### 이벤트란?

- 예외 ❌
    
- 명령 ❌
    
- “어떤 일이 발생했다는 사실 알림”
    

### 이벤트 객체

```java
public class DepositRequestedEvent {
    private final Long transferId;
}
```

- 그냥 POJO
    
- 상속, 인터페이스, 어노테이션 필요 없음
    

---

## 11. 이벤트 매핑 규칙 (중요)

- 타입 기반 매핑
    
- 메서드 파라미터 타입 == 이벤트 타입
    

```java
@TransactionalEventListener
public void onDepositRequested(DepositRequestedEvent event) {
    ...
}
```

- 메서드를 직접 호출하지 않음
    
- publishEvent()가 트리거
    

---

## 12. @TransactionalEventListener 의미

- 기본 phase: AFTER_COMMIT
    
- 이전 트랜잭션이 정상 커밋된 뒤 실행
    
- Saga에 필수
    

```
TX1 (출금) COMMIT
   ↓
TX2 (입금 or 보상) 시작
```

---

## 13. Saga에서 이벤트의 역할

- 단계 간 연결 고리
    
- 함수 직접 호출 ❌
    
- 상태 기반으로 다음 단계 실행
    

---

## 14. 핵심 판단 기준 요약

- 돈 관련 → 비관적 락
    
- 충돌 허용 → 낙관적 락
    
- 외부 API 포함 → Saga
    
- 트랜잭션은 짧게
    
- 상태는 DB에 남긴다
    

---

## 한 문장 요약

트랜잭션으로 안 되는 문제는  
상태 + 이벤트 + 보상으로 푼다

---

# [보조 섹션] 사고의 흐름 복구용 메모 (응답 1 발췌)

## 왜 트랜잭션만으로는 부족한가

- 트랜잭션은 DB 내부까지만 보장
    
- 외부 API, 네트워크 호출은 포함 불가
    
- 이미 나간 요청은 롤백 불가능
    

→ “완벽한 트랜잭션”이라는 가정이 깨짐

---

## 왜 SELECT FOR UPDATE가 필요한가

- UPDATE 전에 SELECT만 하면 동시 접근 가능
    
- 잔액 계산은 읽기 + 쓰기 조합
    
- 중간에 값 바뀌면 금액 꼬임
    

→ 읽는 순간부터 잠가야 함

---

## 낙관적 락 자동 재시도의 진짜 의미

- 재시도 = 실패한 UPDATE만 다시 하는 게 아님
    
- 메서드 전체를 처음부터 다시 실행
    
- 그래서 idempotent가 아니면 위험
    

---

## Saga의 본질

- 트랜잭션을 길게 가져가는 게 아니라
    
- “되돌릴 수 있게 설계”하는 것
    
- 상태 테이블은 로그가 아니라 **진행 기록**
    

---

## 상태 머신이라는 말의 의미

- 지금 단계가 어딘지 DB가 알고 있음
    
- 서버 재시작해도 이어서 처리 가능
    
- 트랜잭션이 아니라 **흐름을 관리**
    

---

## 결론 사고 정리

- 락은 충돌 전략
    
- 트랜잭션은 원자성
    
- 이벤트는 연결
    
- 상태는 복구 수단
    
- Saga는 현실 타협안
    
