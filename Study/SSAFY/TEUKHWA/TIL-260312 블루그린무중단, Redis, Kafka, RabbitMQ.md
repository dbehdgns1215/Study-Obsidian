
## 1. 무중단 배포의 정석: 블루-그린 (Blue-Green)

단순히 "두 대 띄운다"를 넘어, 어떻게 **실수 없이 스위칭**하느냐가 핵심이야.

### 🔹 기본 구조

- **Blue (Active):** 현재 실제 트래픽을 처리 중인 구버전 환경.
    
- **Green (Standby):** 새 코드가 배포되어 검증을 기다리는 신버전 환경.
    
- **로드밸런서 (Nginx):** 사용자의 요청을 Blue 혹은 Green으로 전달하는 게이트웨이.
    

### 🔹 CI/CD 파이프라인의 지엽적 디테일 (Jenkins 기준)

- **상태 인지 (State Awareness):** 스크립트가 `curl`이나 Nginx 설정을 읽어 현재 활성 포트가 `8080`인지 `8081`인지 변수에 담아야 함.
    
- **선택적 배포 (Targeting):** Active가 8080이면, 배포 스크립트는 **오직 8081**만 중지(`docker stop`)시키고 새 이미지를 올림.
    
- **내부 헬스 체크 (Direct Access):** Nginx가 연결하기 전에, 서버 내부에서 `localhost:8081/api/health`를 찔러봐야 함. 여기서 '200 OK'가 안 나오면 배포를 즉시 중단하고 Nginx 설정을 건드리지 않음. (배포 사고 방지)
    
- **Atomic 스위칭:** `sed` 명령어로 Nginx 설정 파일의 포트 번호만 바꾸고 `nginx -s reload` 실행. 이 작업은 1초 미만으로 소요되며 기존 연결을 끊지 않음.
    

---

## 2. 메시지 브로커: Kafka vs RabbitMQ (비교 분석)

### ✉️ RabbitMQ (전달 중심의 스마트 브로커)

- **동작 방식:** **Push Model**. 브로커가 컨슈머의 상태를 봐가며 메시지를 밀어줌.
    
- **메시지 수명:** 컨슈머가 "잘 받았어(ACK)"라고 응답하면 큐에서 **데이터를 즉시 삭제**.
    
- **라우팅의 유연성:** `Exchange`라는 개념이 있어 특정 조건에 맞는 메시지만 특정 큐로 보내는 정교한 필터링이 가능함.
    
- **단점:** 데이터가 사라지기 때문에 장애 복구 시 과거 데이터를 다시 읽을 수 없음.
    

### 📦 Apache Kafka (로그 중심의 분산 스트리밍 플랫폼)

- **동작 방식:** **Pull Model**. 컨슈머가 자기 속도에 맞춰 데이터를 가져감.
    
- **데이터 보존:** 읽어도 안 사라짐. 디스크에 **Append-only Log** 형태로 쌓아두며, 설정한 기간(예: 7일) 동안 보관.
    
- **오프셋 (Offset):** 메시지의 '방 번호'. 컨슈머는 자신이 읽은 마지막 오프셋을 기록해둠.
    
- **복구력 (Replayability):** 서버가 터져도 마지막 오프셋 다음부터 읽으면 끝. 혹은 아예 0번 오프셋부터 다시 읽어서 전체 데이터를 복구할 수도 있음.
	
- 로그(Log)** 또는 **파티션(Partition)**
    
- **오프셋(Offset)**
일반적인 메시지 큐(RabbitMQ 등)는 데이터를 읽어가면 큐에서 데이터를 '삭제(Pop)'해버립니다. 하지만 카프카는 데이터를 지우지 않고 파일(디스크)의 끝에 계속 이어 붙이기만 하는 **'Append-only Log(추가 전용 로그)'** 방식을 사용합니다.

여기서 핵심이 바로 **오프셋(Offset)**입니다.

- 카프카에 메시지가 들어오면 0, 1, 2, 3... 식으로 고유한 방 번호(오프셋)가 붙습니다.
    
- 데이터를 가져가는 쪽(컨슈머)은 **"나 지금 3번 오프셋까지 읽었어"**라고 카프카에 기록(Commit)해 둡니다. 마치 책갈피를 꽂아두는 것과 같습니다.
    
- 만약 서버가 터져서 재부팅되었다면? 컨슈머는 카프카에게 "나 아까 3번까지 읽었으니까, 4번부터 다시 줘!"라고 요청합니다. **실패한 지점부터 완벽하게 재시작(Replay)이 가능**한 이유가 바로 이 오프셋 덕분입니다.


#### ⚙️ 카프카의 3가지 핵심 구성 요소

이 구조를 카프카의 공식 용어로 바꾸면 딱 세 가지만 아시면 됩니다.

1. **프로듀서 (Producer):** 메시지를 생산해서 카프카로 보내는 녀석입니다. (위 예시의 웹 서버)
    
2. **토픽 (Topic):** 카프카 내부의 '주제별 게시판'입니다. 예를 들어 `cover-letter-analyze-events`라는 토픽을 만들어두면, 프로듀서는 이 토픽에 데이터를 넣고 컨슈머는 이 토픽에서 데이터를 빼갑니다.
    
3. **컨슈머 (Consumer):** 카프카의 토픽에 쌓인 메시지를 가져와서 실제 무거운 작업을 처리하는 녀석입니다. (위 예시의 AI 분석 서버)

#### 🚀 백엔드 아키텍처에서 카프카가 주는 압도적 장점

단순히 비동기 처리만 하는 거라면 다른 메시지 큐(RabbitMQ 등)도 있습니다. 하지만 굳이 카프카를 쓰는 이유는 다음과 같습니다.

- **완벽한 디커플링 (모놀리식 -> 마이크로서비스 전환의 핵심):** 웹 서버와 AI 서버, 결제 서버, 알림 서버가 서로 알 필요가 없습니다. 그저 각자 카프카에 메시지를 던지고, 필요한 서버가 가져가면 끝입니다. 한 서버가 배포 중이거나 장애가 나서 꺼져 있어도, 메시지는 카프카에 안전하게 보관되므로 시스템 전체가 뻗는 일이 없습니다.
    
- **미친듯한 처리량 (트래픽 분산과 버퍼링):** 동시성 제어나 락(Lock)을 걸어야 할 만큼 트래픽이 폭주할 때, 카프카가 거대한 '댐(Buffer)' 역할을 해줍니다. 수만 건의 요청이 들어와도 카프카가 다 받아내고, 뒤에 있는 서버나 DB는 본인들이 소화할 수 있는 속도로만 안전하게 데이터를 처리할 수 있습니다.
    
- **데이터 영속성 (디스크에 저장):** 다른 메시지 큐들은 메시지를 소비하면 큐에서 날려버리지만, 카프카는 디스크에 파일 형태로 며칠이고 저장해 둡니다. 장애가 나서 데이터를 놓쳤더라도, 과거로 돌아가서 다시 데이터를 가져와 처리하는 롤백(Replay)이 가능합니다.

### 결론

- **RabbitMQ:** 아주 친절하고 꼼꼼한 **'스마트한 우체부'** (메시지를 정확한 목적지에 확실하게 배달하는 데 집중)
    
- **카프카 (Kafka):** 지워지지 않는 **'거대한 중앙 게시판'** (메시지를 순서대로 쫙 붙여놓고, 필요한 사람들이 알아서 엄청난 속도로 읽어가게 하는 데 집중)

|**구분**|**RabbitMQ**|**Apache Kafka**|
|---|---|---|
|**작동 방식**|**Push (밀어내기):** 우체부가 수신자에게 편지를 직접 배달하듯, 브로커가 컨슈머에게 데이터를 밀어줍니다.|**Pull (당겨오기):** 게시판에 글이 붙어 있으면, 컨슈머들이 자기가 원할 때 원하는 만큼 읽어(당겨) 갑니다.|
|**라우팅(분배) 능력**|**매우 뛰어남:** 'Exchange'라는 기능이 있어, A조건이면 1번 큐로, B조건이면 2번 큐로 아주 복잡하고 섬세하게 나눠서 보낼 수 있습니다.|**단순함:** 'Topic'이라는 하나의 큰 카테고리에 다 때려 넣으면, 읽는 쪽에서 알아서 걸러서 써야 합니다.|
|**메시지 보관 (영속성)**|**읽으면 삭제:** 컨슈머가 메시지를 잘 받았다고 확인(ACK)하면, 큐에서 메시지를 바로 지워버립니다.|**일정 기간 보관:** 메시지를 읽어가도 디스크에 계속 남겨둡니다. (예: 7일간 보관). 언제든 과거로 돌아가 재처리(Replay)가 가능합니다.|
|**처리량 (Throughput)**|초당 수만 건 처리 (충분히 빠름)|초당 수백만 건 처리 (압도적으로 빠름)|

#### RabbitMQ의 장단점

**장점 (Pros)**

- **섬세한 라우팅:** 메시지가 어디로 가야 할지 아주 복잡한 규칙을 설정할 수 있습니다.
    
- **낮은 지연 시간(Low Latency):** 데이터가 들어오자마자 컨슈머에게 즉각 밀어주기 때문에 실시간 처리에 유리합니다.
    
- **편리한 관리:** UI(관리자 페이지)가 기본적으로 잘 되어 있고, 운영 관리가 비교적 쉽습니다.
    

**단점 (Cons)**

- 데이터가 한 번 소비되면 사라지므로, 에러가 났을 때 과거의 데이터를 다시 불러와서 처리(Replay)하기 어렵습니다.
    
- 트래픽이 카프카 수준으로 초대규모로 발생하면 성능 병목이 생길 수 있습니다.
    

#### 카프카의 장단점

**장점 (Pros)**

- **압도적인 대용량 처리:** '파티션(Partition)'을 통해 분산 처리를 극대화하여 트래픽 폭주에도 끄떡없습니다.
    
- **메시지 재처리(Replay) 가능:** 서버에 치명적인 장애가 나서 어제자 데이터를 날렸더라도, 카프카에 저장된 어제 기록부터 다시 쭉 읽어와 복구할 수 있습니다.
    
- **마이크로서비스(MSA)의 뼈대:** 각 서비스가 완전히 독립적으로 움직일 수 있는 완벽한 디커플링을 제공합니다.

**단점 (Cons)**

- **운영 난이도 극상:** 클러스터 구성, 파티션 관리 등 설정하고 운영하는 비용(인적, 리소스적)이 매우 큽니다.
    
- 단순히 서버 두 대 간에 데이터를 주고받는 용도로 쓰기에는 오버스펙(Over-engineering)입니다.

---

## 3. 실시간 통신과 영속성: Redis Pub/Sub vs Kafka

|**구분**|**Redis Pub/Sub**|**Apache Kafka**|
|---|---|---|
|**비유**|라디오 생방송|유튜브/넷플릭스 다시보기|
|**속도**|**In-Memory** 기반이라 극도로 빠름|디스크 쓰기가 수반되나 병렬 처리에 강함|
|**데이터 유실**|수신자가 없으면 **즉시 소멸**|컨슈머가 없어도 **디스크에 저장**|
|**사용 사례**|실시간 채팅, 가벼운 앱 알림|결제 로그, 사용자 활동 트래킹|

---

## 4. Redis (인메모리 데이터 구조 저장소) 깊게 파기

### 🧩 5대 핵심 자료구조의 실무 활용

단순 캐시를 넘어선 **공용 자료구조**로서의 가치:

1. **String:** `SET`, `GET`. 특히 `INCR` 명령어는 **원자적(Atomic)**이라 조회수 중복 증가 문제를 방지함.
    
2. **List:** `LPUSH`, `RPOP`. 작업 대기열(Task Queue)이나 최근 검색어 목록 저장에 유리.
    
3. **Set:** 중복 없는 집합. `SADD`. '오늘 방문한 유저 수(Unique 방문자)' 계산에 최적.
    
4. **Hash:** 객체형 데이터. `HSET`. 유저 프로필처럼 여러 필드(`name`, `email`)를 가진 데이터를 묶어서 관리.
    
5. **Sorted Set (ZSet):** `ZADD`. 데이터에 **Score**를 매김. 게임 랭킹, 실시간 인기 급상승 검색어 등 자동 정렬이 필요한 곳에 필수.
    

### 🧵 싱글 스레드(Single Thread)의 미학

- 레디스는 한 번에 하나의 명령어만 처리함.
    
- **장점:** 복잡한 락(Lock) 없이도 **경쟁 상태(Race Condition)**를 완벽하게 회피함.
    
- **주의:** `keys *` 같이 무거운 명령어를 날리면 그동안 다른 모든 요청이 대기하므로 실무에선 절대 금지.

### ✌️ 자바에서 레디스를 쓰는 2가지 방법

#### 방법 1. `RedisTemplate` 사용 (수동 제어, 디테일한 작업용)

가장 기본적이고 직관적인 방법입니다. 내가 원할 때 직접 키(Key)와 값(Value)을 넣고, 빼고, 만료 시간(TTL)을 설정할 수 있습니다. 예를 들어, **이메일 인증 번호**, **리프레시 토큰**, 혹은 사용자가 **작성 중인 임시 데이터**를 저장할 때 딱 맞습니다.


```Java
import org.springframework.data.redis.core.StringRedisTemplate;
import org.springframework.stereotype.Service;
import java.time.Duration;

@Service
public class RedisService {

    private final StringRedisTemplate redisTemplate;

    public RedisService(StringRedisTemplate redisTemplate) {
        this.redisTemplate = redisTemplate;
    }

    // 데이터 저장하기 (예: 3분 뒤에 자동으로 삭제되는 인증번호)
    public void saveVerificationCode(String email, String code) {
        redisTemplate.opsForValue().set(email, code, Duration.ofMinutes(3));
    }

    // 데이터 꺼내오기
    public String getVerificationCode(String email) {
        return redisTemplate.opsForValue().get(email);
    }
}
```

> **참고:** `opsForValue()`는 레디스의 가장 기본인 String 자료구조를 다룰 때 씁니다. List, Set, Hash 등을 다루는 전용 메서드(`opsForList()`, `opsForHash()` 등)도 모두 지원합니다.

#### 방법 2. `@Cacheable` 어노테이션 사용 (마법 같은 캐싱)

DB에서 매번 똑같은 데이터를 조회해서 가져오면 서버가 무겁고 느려지겠죠? 이때 조회 메서드 위에 어노테이션 하나만 붙이면, **스프링이 알아서 첫 조회 때는 DB에서 가져와 레디스에 저장해 두고, 두 번째부터는 DB를 찌르지 않고 레디스에서 빛의 속도로 꺼내옵니다.**



```Java
import org.springframework.cache.annotation.Cacheable;
import org.springframework.stereotype.Service;

@Service
public class ResumeService {

    // "resume"라는 이름의 캐시 공간에 id를 키(Key)로 써서 저장해라!
    @Cacheable(value = "resume", key = "#id")
    public ResumeDto getResumeById(Long id) {
        // 이 안의 로직은 첫 번째 요청에만 실행되고,
        // 두 번째부터는 실행되지 않고 레디스에서 바로 응답합니다.
        System.out.println("DB에서 자기소개서 정보 조회 중...");
        return resumeRepository.findById(id).orElseThrow();
    }
}
```

### 🔑 공통 메서드 (자료구조 상관없이 사용)

- `redisTemplate.delete(key)`: 특정 키의 데이터 삭제
    
- `redisTemplate.hasKey(key)`: 해당 키가 존재하는지 확인 (boolean 반환)
    
- `redisTemplate.expire(key, 시간)`: 특정 키의 만료 시간 설정
    

### 📝 1) String (가장 기본, 단순 키-값)

메서드: `opsForValue()`

- `set(key, value)`: 값 저장
    
- `set(key, value, 만료시간)`: 값 저장과 동시에 TTL(만료시간) 설정
    
- `setIfAbsent(key, value)`: **(중요)** 해당 키가 없을 때만 값을 저장. (분산 락을 직접 구현할 때 쓰이는 핵심 메서드입니다.)
    
- `get(key)`: 값 조회
    
- `increment(key, 숫자)`: 값을 주어진 숫자만큼 증가 (조회수 증가 등에 유용)
    

### 📚 2) List (순서가 있는 리스트, 큐/스택처럼 활용)

메서드: `opsForList()`

- `rightPush(key, value)`: 리스트의 오른쪽(끝)에 데이터 추가
    
- `leftPop(key)`: 리스트의 왼쪽(처음)에서 데이터 꺼내기 (메시지 큐처럼 쓸 때 사용)
    
- `range(key, 시작인덱스, 끝인덱스)`: 특정 범위의 데이터 목록 조회
    

### 🗂️ 3) Hash (하나의 키 안에 여러 개의 필드-값 쌍을 저장, 객체 형태)

메서드: `opsForHash()`

- `put(key, hashKey, value)`: 특정 해시 키 안에 필드와 값을 저장
    
- `get(key, hashKey)`: 특정 필드의 값 조회
    
- `entries(key)`: 해당 키의 모든 해시 데이터(Map 형태) 조회
    

### 🏆 4) Sorted Set (점수(Score)를 기준으로 자동 정렬되는 셋, 랭킹 보드에 필수)

메서드: `opsForZSet()`

- `add(key, value, score)`: 데이터와 점수를 함께 저장 (저장과 동시에 점수순 정렬됨)
    
- `reverseRange(key, 시작, 끝)`: 점수가 높은 순서대로(내림차순) 데이터 조회 (예: 랭킹 1위~10위 가져오기)


---

## 5. 카프카 내부 메커니즘: 파티션과 스레드

### 🧵 컨슈머 스레드 운영 법칙

- **1:1 매핑:** 같은 컨슈머 그룹 내에서 **하나의 파티션은 오직 한 명의 스레드**만 담당함.
    
- **병렬성 확보:** 처리 속도를 높이고 싶다면 컨슈머 스레드만 늘리는 게 아니라, 카프카 토픽의 **파티션 개수**를 먼저 늘려야 함.
    
- **@KafkaListener:** 스프링 부트에서 컨슈머 스레드 풀을 관리해주며, `concurrency` 설정을 통해 스레드 개수를 조절할 수 있음.

**application.yml** 카프카 우체국(브로커)의 주소를 적어줍니다. (보통 로컬에 도커로 카프카를 띄워서 9092 포트를 씁니다.)

YAML

```
spring:
  kafka:
    bootstrap-servers: localhost:9092
    consumer:
      group-id: my-group # 이 컨슈머가 속한 그룹 이름 (필수)
      auto-offset-reset: earliest # 처음 실행될 때 과거 데이터부터 읽을지(earliest), 지금부터 들어오는 것만 읽을지(latest)
```

### 🚀 2단계: 메시지 보내기 (Producer)

프로듀서는 `KafkaTemplate`을 주입받아서 딱 하나의 주요 메서드인 `send()`만 쓰면 됩니다.

```Java
import org.springframework.kafka.core.KafkaTemplate;
import org.springframework.stereotype.Service;

@Service
public class KafkaProducerService {

    private final KafkaTemplate<String, String> kafkaTemplate;

    public KafkaProducerService(KafkaTemplate<String, String> kafkaTemplate) {
        this.kafkaTemplate = kafkaTemplate;
    }

    public void sendMessage(String message) {
        // "test-topic"이라는 이름의 카프카 게시판에 메시지를 던짐
        kafkaTemplate.send("test-topic", message);
        
        System.out.println("카프카로 메시지 전송 완료: " + message);
    }
}
```

**주요 메서드:**

- `send(토픽이름, 데이터)`: 가장 기본적인 전송 방식.
    
- `send(토픽이름, 키(Key), 데이터)`: 카프카는 파티션(Partition)이라는 여러 개의 방으로 데이터를 나누어 저장하는데, 특정 키를 주면 그 키에 해당하는 데이터는 항상 같은 파티션으로 순서를 보장하며 들어가게 됩니다.
    

### 📥 3단계: 메시지 받기 (Consumer)

컨슈머는 더 쉽습니다. 별도의 설정 클래스 없이 메서드 위에 `@KafkaListener` 어노테이션만 붙여주면, 스프링이 알아서 뒤에서 카프카를 계속 주시하다가 메시지가 들어오면 낚아채 옵니다.

```Java
import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.stereotype.Service;

@Service
public class KafkaConsumerService {

    // "test-topic"에 데이터가 들어오면 이 메서드가 자동으로 실행됨
    @KafkaListener(topics = "test-topic", groupId = "my-group")
    public void consume(String message) {
        System.out.println("카프카에서 메시지 수신: " + message);
        
        // 여기서 무거운 작업(DB 저장, 외부 API 호출 등)을 처리하면 됨
    }
}
```


---

## 6. 데이터 정합성 전략: Write-Back (Redis ➡️ DB)

### 💡 왜 쓰는가? (DB 보호 전략)

DB는 Disk 기반이라 동시에 수천 개의 쓰기 요청이 들어오면 **Lock 경합**으로 전체 시스템이 느려짐. 이를 방지하기 위해 Redis를 '방패'로 사용.

### 🔄 상세 구현 시나리오 (데이터 유실 방지 포함)

1. **쓰기 (Write):** 사용자의 요청(조회수, 임시저장)을 Redis에 즉시 반영. (0.01초 소요)
    
2. **방법 1: 배치 동기화 (Scheduled)**
    
    - `@Scheduled`로 일정 시간마다 Redis 데이터를 긁어옴.
        
    - JPA의 벌크 연산이나 `UPDATE ... SET count = count + :value` 쿼리로 DB에 한 번에 반영.
        
3. **방법 2: 이벤트 기반 동기화 (Kafka)**
    
    - Redis에 데이터를 쓰면서 Kafka에 '변경 이벤트'를 발행.
        
    - 별도의 Consumer 서버가 Kafka 메시지를 하나씩 꺼내 DB에 안전하게 `INSERT/UPDATE`.
        
    - **장점:** DB가 잠깐 죽어도 Kafka에 메시지가 쌓여있어 복구가 완벽함.
        

### ⚠️ 주의: 데이터 증발 방지 (Atomic Operation)

- Redis에서 값을 읽어온 뒤(`GET`) DB에 넣고 Redis 값을 지울 때(`DEL`), 그 사이에 새로 들어온 데이터가 지워질 수 있음.
    
- 해결책: 데이터를 읽어올 때 기존 키를 다른 이름으로 `RENAME` 하거나, Redis의 **Lua Script**를 사용하여 읽기와 삭제를 하나의 원자적 작업으로 묶어야 함.
    

