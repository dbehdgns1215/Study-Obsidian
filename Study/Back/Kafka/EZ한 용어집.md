
# 정말로 EZ 합니다.

## 클러스터

### 브로커
- Kafka 데이터를 저장하고 Producer·Consumer 요청을 처리하는 서버.

### 클러스터
- 여러 Kafka Broker를 하나로 묶은 시스템.

### 부트스트랩 서버
- 클라이언트가 Kafka Cluster에 처음 접속할 때 사용하는 Broker 주소.

### 메타데이터
- Broker, Topic, Partition, Leader와 Replica의 위치 정보.

### ZooKeeper
- 과거 Kafka 외부에서 메타데이터와 Controller 선출을 관리하던 시스템.

### KRaft
- ZooKeeper 없이 Kafka 내부에서 메타데이터를 관리하는 방식.

### 컨트롤러
- Broker 상태를 관리하고 Partition Leader 선출을 조율하는 역할.

### 액티브 컨트롤러
- 현재 클러스터의 메타데이터 변경을 주도하는 Controller 한 대.

### 스탠바이 컨트롤러
- 메타데이터를 복제하며 Active Controller 장애에 대비하는 Controller.

### 컨트롤러 쿼럼
- Active Controller를 선출하고 메타데이터에 합의하는 Controller 집합.

### Raft
- 과반수 합의로 Leader를 선출하고 로그를 복제하는 알고리즘.

### Combined Mode
- Kafka Node 하나가 Broker와 Controller 역할을 함께 맡는 구성.

### Dedicated Controller
- Broker 역할 없이 Controller 역할만 담당하는 Node.

### `node.id`
- KRaft Cluster 안에서 Kafka Node를 구분하는 고유 번호.

### `process.roles`
- Kafka Node가 Broker, Controller 또는 두 역할을 모두 맡을지 정하는 값.

### `controller.quorum.voters`
- Controller 선거에 참여할 Node ID와 접속 주소 목록.

### `listeners`
- Broker가 실제로 연결 요청을 기다릴 내부 주소와 Port.

### `advertised.listeners`
- Broker가 Producer와 Consumer에게 접속하라고 알려 주는 주소와 Port.

### `num.network.threads`
- Broker가 Client의 네트워크 요청을 받고 응답하는 Thread 수. 기본값은 `3`.

### `num.io.threads`
- Broker가 디스크 읽기와 쓰기 등 요청을 처리하는 Thread 수. 기본값은 `8`.

---

## 데이터 저장

### 레코드
- Kafka가 저장하고 전달하는 메시지 한 건.

### 토픽
- 같은 종류의 Record를 모아 놓는 논리적인 공간.

### 파티션
- Topic의 Record를 나누어 저장하는 순서 보장 및 병렬 처리 단위.

### 세그먼트
- Partition의 로그를 일정 크기나 시간으로 나눈 실제 파일 단위.

### 오프셋
- Partition 안에서 Record의 위치를 나타내는 번호.

### 리텐션
- Record를 Kafka에 얼마나 오래 보관할지 정하는 정책.

### 리더 파티션
- 해당 Partition의 읽기와 쓰기를 담당하는 복제본.

### 팔로워 파티션
- Leader의 데이터를 복제하며 장애에 대비하는 복제본.

### 리플리케이션 팩터
- Leader를 포함해 Partition을 총 몇 개의 복제본으로 보관할지 나타내는 값.

### ISR
- Leader를 허용 범위 안에서 정상적으로 따라가고 있는 Replica 목록.

### `min.insync.replicas`
- 쓰기를 허용하기 위해 필요한 최소 ISR 수.

### `num.partitions`
- 자동 생성되는 Topic의 기본 Partition 수. 기본값은 `1`, Plys는 `3`.

### `default.replication.factor`
- 자동 생성되는 Topic의 기본 Replication Factor. 기본값은 `1`, Plys는 `3`.

### `auto.create.topics.enable`
- 존재하지 않는 Topic 요청이 들어왔을 때 Broker가 Topic을 자동 생성할지 정하는 값. 기본값은 `true`.

### `unclean.leader.election.enable`
- ISR이 모두 사라졌을 때 동기화되지 않은 Replica를 Leader로 선출할지 정하는 값. 기본값은 `false`.

### `log.cleanup.policy`
- 보관 기간에 따라 지우는 `delete`와 Key별 최신값을 남기는 `compact` 중 정리 방식을 정하는 값. 기본값은 `delete`.

### `log.retention.hours`
- Broker 로그를 보관하는 기본 시간. 기본값은 `168시간`, 즉 7일.

### `log.segment.bytes`
- Partition 로그 Segment 파일 하나의 목표 최대 크기. 기본값은 `1 GiB`.

### `message.max.bytes`
- Broker가 허용하는 Record Batch의 최대 크기. 기본값은 약 `1 MiB`.

---

## Producer

### 프로듀서
- Kafka Topic에 Record를 발행하는 클라이언트.

### 메시지 키
- Record의 Partition을 결정하고 같은 Key의 순서를 유지하는 데 사용하는 값.

### 직렬화
- Java 객체를 네트워크로 전송할 Byte Array로 변환하는 과정.

### 파티셔너
- Record를 어느 Partition으로 보낼지 결정하는 구성 요소.

### 레코드 어큐뮬레이터
- 전송할 Record를 Partition별로 잠시 모아 두는 Producer 버퍼.

### 배치
- 같은 Partition으로 보낼 여러 Record를 묶은 전송 단위.

### `batch.size`
- Producer Batch의 목표 최대 크기. 기본값은 `16 KiB`.

### `linger.ms`
- Batch에 Record를 더 모으기 위해 기다리는 최대 시간. Kafka 3.8 기본값은 `0ms`.

### Sender Thread
- Accumulator의 Batch를 Broker로 전송하는 백그라운드 Thread.

### `acks`
- Producer가 어느 수준의 저장 확인을 받아야 성공으로 판단할지 정하는 값. 기본값은 `all`.

### 콜백
- Kafka 전송 성공 또는 실패 이후 자동으로 실행되는 코드.

### Producer 멱등성
- Producer 재시도로 동일 Record가 중복 저장되는 것을 줄이는 기능.

### `retries`
- 일시적 전송 실패가 발생했을 때 Producer가 다시 전송하는 최대 횟수. 기본값은 `2147483647`, Plys는 `3`.

### `max.in.flight.requests.per.connection`
- Broker 응답을 기다리면서 동시에 보낼 수 있는 요청 수. 기본값과 Plys 설정은 `5`.

### `delivery.timeout.ms`
- 재시도와 대기를 포함해 Record 전송을 완료할 수 있는 전체 제한 시간. 기본값은 `120000ms`.

### `request.timeout.ms`
- Producer가 Broker의 한 번의 요청 응답을 기다리는 제한 시간. 기본값은 `30000ms`.

### `buffer.memory`
- 아직 전송하지 않은 Record를 모아 두는 Producer 전체 버퍼 크기. 기본값은 `32 MiB`.

### `max.block.ms`
- Producer Buffer가 가득 찼을 때 `send()`가 공간을 기다릴 수 있는 최대 시간. 기본값은 `60000ms`.

### `compression.type`
- Record Batch를 압축할 방식을 정하는 값. 기본값은 `none`.

---

## Consumer

### 컨슈머
- Kafka Topic의 Record를 가져와 처리하는 클라이언트.

### 컨슈머 그룹
- 하나의 목적을 위해 Partition을 나누어 처리하는 Consumer 집합.

### 파티션 독점
- 같은 Consumer Group에서는 Partition 하나를 Consumer 한 명만 담당하는 규칙.

### 리밸런싱
- Consumer 변화에 따라 Partition 담당자를 다시 배정하는 과정.

### 커밋 오프셋
- Consumer Group이 처리를 완료했다고 Kafka에 기록한 다음 위치.

### Consumer Lag
- 최신 Offset과 Committed Offset 사이의 처리되지 않은 Record 수.

### 자동 커밋
- Kafka Client가 Offset을 주기적으로 자동 저장하는 방식.

### Manual ACK
- 업무 처리가 끝난 뒤 애플리케이션이 직접 Offset Commit을 요청하는 방식.

### `__consumer_offsets`
- Consumer Group의 Committed Offset을 저장하는 Kafka 내부 Topic.

### `group.id`
- Consumer가 어느 Consumer Group에 속하는지 구분하는 이름.

### `session.timeout.ms`
- Heartbeat가 끊긴 Consumer를 장애로 판단하기까지 기다리는 시간. Kafka 3.8 기본값은 `45000ms`.

### `heartbeat.interval.ms`
- Consumer가 Group Coordinator에게 생존 신호를 보내는 간격. 기본값은 `3000ms`.

### `max.poll.interval.ms`
- Consumer가 다음 `poll()`을 호출하지 않아도 허용되는 최대 시간. 기본값은 `300000ms`.

### `max.poll.records`
- 한 번의 `poll()`이 애플리케이션에 넘겨주는 최대 Record 수. 기본값은 `500`.

### `fetch.min.bytes`
- Broker가 Fetch 응답을 보내기 전에 모으려는 최소 데이터 크기. 기본값은 `1 Byte`.

### `fetch.max.wait.ms`
- `fetch.min.bytes`가 채워지지 않아도 Broker가 Fetch 응답을 보내는 최대 대기 시간. 기본값은 `500ms`.

### `max.partition.fetch.bytes`
- Consumer가 한 번의 Fetch에서 Partition 하나당 받을 데이터의 목표 최대 크기. 기본값은 `1 MiB`.

### `fetch.max.bytes`
- Consumer가 한 번의 Fetch 응답 전체에서 받을 데이터의 목표 최대 크기. 기본값은 `50 MiB`.

### `enable.auto.commit`
- Consumer가 Offset을 주기적으로 자동 Commit할지 정하는 값. 기본값은 `true`, Plys는 `false`.

### `auto.commit.interval.ms`
- 자동 Commit을 사용할 때 Offset을 Commit하는 주기. 기본값은 `5000ms`.

### `auto.offset.reset`
- 저장된 Offset이 없거나 유효하지 않을 때 읽기를 시작할 위치. 기본값은 `latest`, Plys는 `earliest`.

### `partition.assignment.strategy`
- Consumer Group 안에서 Partition을 Consumer에게 나누는 방식.

### `group.instance.id`
- Consumer를 고정 멤버로 식별해 짧은 재시작으로 인한 Rebalance를 줄이는 값. 기본값은 `null`.

### `isolation.level`
- Kafka Transaction에서 Commit된 Record만 읽을지 결정하는 값. 기본값은 `read_uncommitted`.

---

## 처리 보장

### At-Most-Once
- 중복은 줄이지만 실패한 메시지가 유실될 수 있는 처리 방식.

### At-Least-Once
- 유실은 줄이지만 같은 메시지가 중복 처리될 수 있는 방식.

### Exactly-Once
- 재시도가 발생해도 결과가 논리적으로 한 번만 반영되는 처리 방식.

### 멱등성
- 같은 작업을 여러 번 수행해도 최종 결과가 달라지지 않는 성질.

### Kafka Transaction
- 여러 Kafka 발행과 Offset Commit을 하나의 작업으로 묶는 기능.

### DB Transaction
- 여러 DB 작업을 모두 Commit하거나 모두 Rollback하도록 묶는 기능.

### 원자성
- 여러 작업이 전부 성공하거나 전부 실패해야 하는 성질.

### DLT
- 계속 실패하는 메시지를 따로 격리하는 Dead Letter Topic.

### 재시도
- 일시적인 실패가 발생한 작업을 다시 수행하는 처리.

---

## 시스템 연동

### Dual Write
- 하나의 요청에서 DB 저장과 Kafka 전송을 각각 수행하는 구조.

### Outbox Pattern
- 업무 데이터와 발행할 이벤트를 같은 DB Transaction으로 저장하는 패턴.

### Inbox Pattern
- 처리한 Event ID를 DB에 기록해 Consumer 중복 처리를 막는 패턴.

### Event ID
- 메시지 한 건을 고유하게 식별하는 값.

### CDC
- DB 변경 로그를 읽어 변경 내용을 이벤트로 전달하는 기술.

### Binlog
- MySQL의 데이터·스키마 변경 이력을 기록하는 Binary Log.

### Kafka Connect
- Kafka와 DB 등 외부 시스템 사이의 데이터 이동을 관리하는 플랫폼.

### Debezium
- DB의 Binlog를 읽어 변경 이벤트를 Kafka로 보내는 CDC Connector.

---

## Plys 연관 개념

### `@Transactional`
- Spring에서 DB Transaction의 범위를 지정하는 Annotation.

### Master DB
- 쓰기와 최신 데이터 조회를 담당하는 원본 DB.

### Slave DB
- Master 데이터를 복제해 주로 조회를 처리하는 DB.

### Read/Write Splitting
- 쓰기는 Master, 읽기는 Slave로 보내는 구조.

### Replication Lag
- Master의 변경이 Slave에 반영되기까지 발생하는 시간 차.

### Read-After-Write
- 데이터를 쓴 직후 조회했을 때 최신 데이터가 보여야 하는 정합성.

### ThreadLocal
- 현재 Thread 안에서만 공유되는 값을 저장하는 Java 기능.

### RoutingDataSource
- 트랜잭션 상태에 따라 Master와 Slave를 선택하는 DataSource.

---

## Elasticsearch 비교

### Elasticsearch Index
- 비슷한 JSON Document를 모아 놓는 논리적인 공간.

### Shard
- Elasticsearch Index의 Document를 나누어 저장하는 단위.

### Sharding
- 여러 Document를 여러 Primary Shard로 분배하는 것.

### Replica Shard
- Elasticsearch Primary Shard의 복사본.

### Lucene Index
- Elasticsearch Shard 내부에서 실제 검색과 역인덱싱을 수행하는 저장소.






# 아래는 조금 심화 버전

## 1. 시스템 인프라 아키텍처

### Kafka Cluster
- 같은 클러스터로 묶인 Broker와 Controller의 집합이다. Topic과 Partition을 분산 저장하고 장애가 발생하면 Leader를 재선출한다.

### Broker
- Kafka Record를 실제 디스크에 저장하고 Producer·Consumer의 요청을 처리하는 Kafka 서버 프로세스다.

### Bootstrap Server
- 클라이언트가 Kafka Cluster에 처음 접속할 때 사용하는 Broker 주소 목록이다. 모든 Broker를 적을 필요는 없지만 일부 장애를 고려해 여러 주소를 지정한다.

```
Bootstrap Broker 접속
→ Cluster Metadata 조회
→ Partition Leader 확인
→ 실제 Leader Broker와 통신
```

### Cluster Metadata
- Broker, Topic, Partition, Leader, Replica, ISR 등 Kafka Cluster의 현재 구조를 나타내는 정보다.

---

## 1.1 메타데이터 관리 시스템

### ZooKeeper
- 과거 Kafka 외부에서 Broker 등록, Controller 선출과 일부 클러스터 메타데이터 관리를 담당하던 분산 코디네이터다. Record 자체는 ZooKeeper가 아니라 Kafka Broker에 저장됐다.

### KRaft
- ZooKeeper 없이 Kafka 내부의 Controller Quorum과 Raft 기반 Metadata Log로 클러스터 상태를 관리하는 방식이다.

### Metadata Log
- Controller들이 Broker·Topic·Partition 상태의 변경 이력을 순서대로 기록하고 복제하는 내부 로그다.

---

## 1.2 클러스터 통제 엔진

### Controller
- Broker 등록, Partition Leader 선출, Replica 배치 등 클러스터의 메타데이터를 관리하는 Kafka 역할이다.

### Controller Quorum
- KRaft Metadata Log를 복제하고 Active Controller를 선출하는 Controller들의 집합이다.

### Active Controller
- Controller Quorum의 현재 Leader다. 메타데이터 변경을 주도하고 Broker 장애가 발생하면 필요한 Partition Leader 선출을 조율한다.

### Standby Controller
- Active Controller의 Metadata Log를 복제하며 대기하는 Controller다. Active 장애 시 새로운 Active 후보가 된다.

### Raft 합의 알고리즘
- Controller들이 동일한 Metadata Log 상태를 유지하고 과반수 투표로 Active Controller를 선출하는 원리다. Leader 선출뿐 아니라 로그 복제와 Commit 여부도 관리한다.

### Quorum
- 합의를 성립시키는 데 필요한 과반수다.

```
Controller 3대 → 최소 2대 필요 → 1대 장애 허용
Controller 5대 → 최소 3대 필요 → 2대 장애 허용
```

### Combined Mode
- 하나의 Kafka 프로세스가 Broker와 Controller를 동시에 담당하는 구성이다.

```
process.roles=broker,controller
```

Plys의 Kafka 3대는 모두 Combined Mode다. 세 노드 중 하나가 Active Controller, 나머지가 Standby Controller가 된다.

### Dedicated Controller
- Broker 역할 없이 Controller만 담당하는 Kafka Node다. 중요 운영 환경에서는 Broker 부하와 Controller를 격리하고 독립적으로 확장하기 위해 사용한다.

### `node.id`
- KRaft Cluster에서 Kafka Node를 구분하는 고유 번호다.

### `controller.quorum.voters`
- Controller 선거에 참여하는 Node ID와 주소를 지정하는 설정이다.

```
1@kafka-1:9093,2@kafka-2:9093,3@kafka-3:9093
```

### Control Plane
- Controller가 Metadata, Broker 상태와 Leader 선출을 관리하는 경로다.

### Data Plane
- Producer의 Record가 Partition Leader에 저장되고 Consumer에게 전달되는 실제 데이터 경로다.

---

## 1.3 KRaft와 Broker 연결 설정

| 설정 | Kafka 3.8.1 기본값 | Plys 설정 | 역할과 주의점 |
|---|---:|---:|---|
| `node.id` | 없음 | `1`, `2`, `3` | KRaft Node의 고유 ID다. 같은 Cluster 안에서 중복되면 안 된다. |
| `process.roles` | 없음 | `broker,controller` | KRaft에서 Node의 역할을 정한다. Plys는 세 Node가 두 역할을 겸한다. |
| `controller.quorum.voters` | 없음 | `1@...:9093,2@...:9093,3@...:9093` | Controller Quorum 구성원의 ID와 주소다. Kafka 3.8의 정적 Quorum에서는 직접 지정한다. |
| `controller.listener.names` | 없음 | `CONTROLLER` | Controller 통신에 사용할 Listener 이름이다. |
| `listeners` | `PLAINTEXT://:9092` | `PLAINTEXT://:9092,CONTROLLER://:9093` | Broker 프로세스가 실제로 연결을 기다리는 주소다. |
| `advertised.listeners` | `null` | Node별 `plys-kafka-N:9092` | Client에게 알려 주는 접속 주소다. Docker 내부 DNS나 외부 접속 주소와 맞지 않으면 Bootstrap 이후 연결에 실패한다. |
| `num.network.threads` | `3` | 기본값 사용 | Client 요청을 받고 응답을 보내는 Network Thread 수다. |
| `num.io.threads` | `8` | 기본값 사용 | 디스크 I/O와 요청 처리를 수행하는 Thread 수다. |
| `socket.request.max.bytes` | `104857600` (100 MiB) | 기본값 사용 | Broker가 받을 수 있는 요청 하나의 최대 크기다. 메모리 사용량과 함께 조정해야 한다. |

`listeners`와 `advertised.listeners`는 역할이 다르다.

```text
listeners
→ Broker가 실제로 Bind할 주소

advertised.listeners
→ Metadata를 통해 Client에게 알려 줄 주소
```

---

## 2. 데이터 저장 구조

### Topic
- Record를 업무 종류별로 분류하는 논리적 공간이다. Cluster 아래에서 데이터를 구분하는 가장 큰 논리 단위다.

### Record
- Kafka가 저장하고 전달하는 메시지 한 건이다.

```
Key + Value + Timestamp + Headers
```

### Partition
- Topic의 Record를 나누어 저장하는 Append-only 로그이자 병렬 처리 단위다. Kafka의 순서는 Topic 전체가 아니라 Partition 내부에서만 보장된다.

```
Topic
├─ Partition 0: A → C → F
├─ Partition 1: B → E
└─ Partition 2: D → G
```

Record 하나를 여러 Partition으로 쪼개는 것이 아니라, Record 전체가 특정 Partition 하나에 저장된다.

### Segment
- Partition의 로그를 일정 크기나 시간 단위로 나눈 실제 파일 묶음이다. Partition 하나가 영원히 커지는 파일 하나로 저장되는 것은 아니다.

### Offset
- Partition 안에서 Record의 위치를 나타내는 번호다. Partition마다 0부터 독립적으로 증가한다.

```
Partition 0: Offset 0, 1, 2
Partition 1: Offset 0, 1, 2
```

### Retention
- Record를 Kafka에 얼마나 오래 보관할지 정하는 정책이다. Consumer가 읽었다고 Record가 즉시 삭제되지는 않는다.

---

## 2.1 고가용성과 복제

### Partition Leader
- 해당 Partition의 일반적인 읽기와 쓰기를 담당하는 Broker의 Partition 복제본이다.

### Partition Follower
- Leader의 Record를 Fetch해 복제하는 Partition 복제본이다. 정상적으로 동기화된 Follower는 Leader 장애 시 승격 후보가 된다.

### Replication Factor
- Leader를 포함해 동일 Partition을 총 몇 개의 복제본으로 보관할지 나타내는 값이다.

```
Replication Factor 3
= Leader 1개 + Follower 2개
= 총 3사본
```

### ISR
- `In-Sync Replicas`의 약자다. 설정된 허용 지연 범위 안에서 Leader를 따라가고 있는 Replica 집합이다.

100% 같은 Offset이어야만 ISR인 것은 아니다. 일정 시간 이상 Leader를 따라오지 못하면 ISR에서 제외된다.

### `min.insync.replicas`
- `acks=all`을 사용하는 Producer의 쓰기를 허용하기 위해 필요한 최소 ISR 수다. Leader도 ISR 수에 포함된다.

```
Replication Factor = 3
min.insync.replicas = 2
```

ISR이 2개 이상이면 쓰기를 허용하지만, 1개만 남으면 데이터 안전성을 위해 쓰기를 거부한다.

### Unclean Leader Election
- ISR이 모두 사라졌을 때 ISR 밖의 Replica를 Leader로 승격하는 선택이다. 가용성은 높일 수 있지만 복제되지 않은 Record를 잃을 수 있다.

---

## 2.2 Broker와 Topic 저장 설정

| 설정 | Kafka 3.8.1 기본값 | Plys 설정 | 역할과 주의점 |
|---|---:|---:|---|
| `num.partitions` | `1` | `3` | 자동 생성 Topic의 기본 Partition 수다. 이미 만들어진 Topic의 Partition 수를 줄이지는 못한다. |
| `default.replication.factor` | `1` | `3` | 자동 생성 Topic의 기본 복제본 수다. Broker 수보다 크게 설정할 수 없다. |
| `min.insync.replicas` | `1` | `2` | `acks=all` 쓰기에 필요한 최소 ISR 수다. Plys는 복제본 3개 중 ISR 2개 이상을 요구한다. |
| `auto.create.topics.enable` | `true` | 기본값 사용 | 잘못 적은 Topic 이름도 새 Topic으로 생길 수 있어 운영에서는 명시적 생성을 선호한다. |
| `unclean.leader.election.enable` | `false` | 기본값 사용 | ISR 밖 Replica의 Leader 승격을 막아 데이터 유실 가능성을 낮춘다. |
| `log.cleanup.policy` | `delete` | 기본값 사용 | 시간·용량 기준 삭제는 `delete`, Key별 최신값 유지는 `compact`다. 함께 지정할 수도 있다. |
| `log.retention.hours` | `168` (7일) | `168` | Broker의 기본 Record 보관 시간이다. Consumer가 읽었는지와 무관하다. |
| `log.retention.bytes` | `-1` | 기본값 사용 | Partition당 용량 제한이다. `-1`은 용량만으로 삭제하지 않는다는 뜻이다. |
| `log.segment.bytes` | `1073741824` (1 GiB) | 기본값 사용 | Segment 파일 하나의 목표 최대 크기다. Retention 삭제는 Segment 단위로 일어난다. |
| `log.retention.check.interval.ms` | `300000` (5분) | 기본값 사용 | 삭제할 Segment가 있는지 확인하는 주기다. 보관 시간이 끝난 즉시 삭제된다는 뜻은 아니다. |
| `message.max.bytes` | `1048588` (약 1 MiB) | 기본값 사용 | Broker가 허용하는 Record Batch 최대 크기다. Producer와 Consumer의 크기 설정도 함께 맞춰야 한다. |
| `replica.fetch.max.bytes` | `1048576` (1 MiB) | 기본값 사용 | Follower가 Partition 하나에서 복제할 때 받는 목표 최대 크기다. |
| `replica.lag.time.max.ms` | `30000` (30초) | 기본값 사용 | Follower가 이 시간 동안 Leader를 따라오지 못하면 ISR에서 제외될 수 있다. |
| `num.replica.fetchers` | `1` | 기본값 사용 | Broker별 Source Broker에서 복제 데이터를 가져오는 Fetcher Thread 수다. |

내부 Topic도 복제 설정을 가진다.

| 설정 | Kafka 3.8.1 기본값 | Plys 설정 | 역할 |
|---|---:|---:|---|
| `offsets.topic.num.partitions` | `50` | 기본값 사용 | `__consumer_offsets`의 Partition 수다. |
| `offsets.topic.replication.factor` | `3` | `3` | Consumer Offset을 저장하는 내부 Topic의 복제본 수다. |
| `transaction.state.log.num.partitions` | `50` | 기본값 사용 | Kafka Transaction 상태 Topic의 Partition 수다. |
| `transaction.state.log.replication.factor` | `3` | `3` | Transaction 상태 Topic의 복제본 수다. |
| `transaction.state.log.min.isr` | `2` | `2` | Transaction 상태를 기록할 때 필요한 최소 ISR 수다. |

Topic별 설정은 Broker 기본값을 덮어쓸 수 있다.

| Topic 설정 | Kafka 3.8.1 기본값 | 대응하는 Broker 기본 설정 | 역할 |
|---|---:|---|---|
| `cleanup.policy` | `delete` | `log.cleanup.policy` | 이 Topic의 삭제 또는 압축 정책이다. |
| `retention.ms` | `604800000` (7일) | `log.retention.ms`·`log.retention.hours` | 이 Topic의 시간 기준 보관 기간이다. `-1`이면 시간 제한이 없다. |
| `retention.bytes` | `-1` | `log.retention.bytes` | 이 Topic의 Partition별 용량 제한이다. |
| `segment.bytes` | `1073741824` (1 GiB) | `log.segment.bytes` | 이 Topic의 Segment 목표 크기다. |
| `max.message.bytes` | `1048588` (약 1 MiB) | `message.max.bytes` | 이 Topic이 허용하는 Record Batch 최대 크기다. |
| `min.insync.replicas` | `1` | `min.insync.replicas` | 이 Topic의 `acks=all` 쓰기에 필요한 최소 ISR 수다. |

---

## 3. Producer 데이터 송신

### Producer
- Record를 생성해 Topic의 Partition Leader에게 전송하는 Kafka Client다.

### Message Key
- Record와 함께 전송되는 값으로, 기본 Partitioner가 Partition을 결정할 때 사용한다.

고유한 값일 필요는 없다. 중요한 성질은 **같은 Key가 일반적으로 같은 Partition으로 들어간다**는 점이다.

```
playlistUid="A" → Partition 1
playlistUid="A" → Partition 1
```

Partition 수를 변경하면 기존과 다른 Partition이 선택될 수 있다.

### Serializer
- Java 객체를 Kafka가 네트워크로 전송할 수 있는 Byte Array로 변환한다.

```
String → StringSerializer
TrackEvent → JsonSerializer
```

### Partitioner
- Topic, Key와 Cluster Metadata를 바탕으로 Record를 보낼 Partition을 선택하는 Producer 구성 요소다.

### Record Accumulator
- Producer가 전송할 Record를 Partition별 Batch로 모아 두는 메모리 버퍼다.

### Batch
- 같은 Partition으로 보낼 여러 Record를 묶은 전송 단위다. Batch로 보내면 네트워크 요청 횟수와 오버헤드를 줄일 수 있다.

### `batch.size`
- Partition별 Batch가 사용할 목표 최대 크기를 지정한다. 이 크기를 채우지 않아도 `linger.ms`가 지나면 전송할 수 있다.

### `linger.ms`
- Batch를 더 채우기 위해 Producer가 기다릴 수 있는 최대 시간이다.

```
작게 설정 → 낮은 지연, 작은 Batch
크게 설정 → 높은 처리량, 추가 지연 가능
```

### Sender Thread
- Record Accumulator의 Batch를 가져와 Partition Leader에게 네트워크 요청을 보내는 Producer의 백그라운드 Thread다.

### `acks`
- Producer가 Record 전송을 성공으로 판단하기 위해 기다릴 Broker 확인 수준이다.

```
acks=0   → Broker 응답을 기다리지 않음
acks=1   → Leader 저장 확인
acks=all → 현재 ISR의 저장 확인
```

### Retry
- 일시적인 네트워크 오류나 Leader 변경이 발생했을 때 Producer가 Record를 다시 보내는 동작이다.

### Callback
- 비동기 전송이 성공하거나 실패했을 때 실행되는 코드다. Plys에서는 `CompletableFuture.whenComplete()`를 사용한다.

### Producer Idempotence
- Producer 재시도로 같은 Record가 Broker에 중복 기록되는 일을 줄이는 기능이다.

```
enable.idempotence=true
```

Producer ID와 Sequence Number를 이용한다. Consumer의 DB 중복 저장까지 막아 주지는 않는다.

---

## 3.1 Producer 핵심 설정

| 설정 | Kafka 3.8.1 기본값 | Plys 설정 | 역할과 주의점 |
|---|---:|---:|---|
| `acks` | `all` | `all` | 현재 ISR의 확인을 기다린다. 실제 쓰기 허용 여부는 `min.insync.replicas`와 함께 결정된다. |
| `enable.idempotence` | `true` | `true` | Producer 재시도로 Broker 로그에 중복 기록되는 일을 줄인다. |
| `retries` | `2147483647` | `3` | 재시도 횟수다. 실제 전송 가능 시간은 `delivery.timeout.ms`에도 제한된다. |
| `max.in.flight.requests.per.connection` | `5` | `5` | 응답을 기다리며 동시에 보낼 요청 수다. 멱등성을 사용할 때 `5` 이하여야 한다. |
| `batch.size` | `16384` (16 KiB) | 기본값 사용 | Partition별 Batch의 목표 최대 크기다. Record 하나가 이보다 크면 해당 Record 크기에 맞춰 Batch가 만들어질 수 있다. |
| `linger.ms` | `0` | 기본값 사용 | Batch를 더 모으기 위한 대기 시간이다. 값을 늘리면 처리량은 좋아질 수 있지만 지연이 추가된다. |
| `buffer.memory` | `33554432` (32 MiB) | 기본값 사용 | 아직 Broker로 보내지 않은 Record를 보관하는 Producer 전체 버퍼다. |
| `max.block.ms` | `60000` (60초) | 기본값 사용 | Buffer 부족이나 Metadata 조회 때문에 `send()` 등이 Block될 수 있는 최대 시간이다. |
| `compression.type` | `none` | 기본값 사용 | `gzip`, `snappy`, `lz4`, `zstd` 등을 사용하면 네트워크와 저장 공간을 줄이는 대신 CPU를 더 쓸 수 있다. |
| `max.request.size` | `1048576` (1 MiB) | 기본값 사용 | Producer 요청 하나의 최대 크기다. Broker의 `message.max.bytes`와 함께 확인한다. |
| `request.timeout.ms` | `30000` (30초) | 기본값 사용 | Broker의 요청 응답 한 번을 기다리는 시간이다. |
| `delivery.timeout.ms` | `120000` (2분) | 기본값 사용 | 전송 대기, 요청과 재시도를 모두 포함한 Record 전달의 전체 제한 시간이다. |

세 시간 설정은 범위가 다르다.

```text
request.timeout.ms
→ Broker 요청 한 번의 응답 대기 시간

delivery.timeout.ms
→ Batch가 만들어진 뒤 성공 또는 실패가 확정될 때까지의 전체 시간

max.block.ms
→ Buffer와 Metadata를 기다리느라 애플리케이션 호출이 막힐 수 있는 시간
```

`KafkaTemplate.send()`가 비동기라는 사실과 Broker 저장 성공은 같은 말이 아니다. HTTP 성공을 Broker 저장 성공 뒤에 보내려면 반환된 Future의 성공을 확인해야 한다.

---

## 4. Consumer 데이터 수신

### Consumer
- Topic의 Partition Leader에서 Record를 Fetch하고 업무 로직을 수행하는 Kafka Client다.

### Consumer Group
- 하나의 목적을 위해 Topic의 Partition을 나누어 처리하는 Consumer들의 집합이다.

### Partition 독점 규칙
- 동일한 Consumer Group 안에서는 Partition 하나를 동시에 Consumer 한 명만 담당한다.

```
Partition 3개 + Consumer 2개
Consumer A → Partition 0, 1
Consumer B → Partition 2
```

Consumer가 Partition보다 많으면 남는 Consumer는 아무 작업도 하지 않는다.

### Group Coordinator
- Consumer Group의 가입, Heartbeat, Offset Commit과 Rebalance를 조율하는 Broker다.

### Rebalance
- Consumer가 추가·제거되거나 Partition 수가 변할 때 Partition 담당자를 다시 배정하는 과정이다.

### Committed Offset
- Consumer Group이 처리를 완료했다고 Kafka에 기록한 위치다. 일반적으로 **마지막 처리 Record가 아니라 다음에 읽을 Offset**을 의미한다.

```
Offset 7까지 처리 완료
→ Committed Offset 8
```

### `__consumer_offsets`
- Consumer Group의 Committed Offset과 Group Metadata를 저장하는 Kafka 내부 Topic이다.

### Auto Commit
- Kafka Client가 일정 주기로 Offset을 자동 Commit하는 방식이다. 업무 처리가 끝나기 전에 Commit될 위험이 있다.

### Manual ACK
- 업무 처리가 끝난 뒤 애플리케이션이 직접 `acknowledge()`를 호출해 Offset Commit을 요청하는 방식이다.

### Consumer Lag
- Partition의 최신 Offset과 Consumer Group의 Committed Offset 차이다.

```
Latest Offset 1,000
Committed Offset 700
Consumer Lag 300
```

Lag이 증가한다는 것은 Consumer 처리가 Producer의 유입 속도를 따라가지 못한다는 뜻이다.

### `auto.offset.reset`
- Consumer Group에 저장된 Offset이 없을 때 어디서부터 읽을지 정한다.

```
earliest → 가장 오래된 보존 Record부터
latest   → 새로 들어오는 Record부터
```

---

## 4.1 Consumer 생존 판정과 Poll 설정

| 설정 | Kafka 3.8.1 기본값 | Plys 설정 | 역할과 주의점 |
|---|---:|---:|---|
| `group.id` | `null` | `plys-consumer-group` | Consumer Group 식별자다. `subscribe()`와 Group Offset 관리를 사용한다면 필요하다. |
| `session.timeout.ms` | `45000` (45초) | 기본값 사용 | Heartbeat가 끊긴 Consumer를 장애로 판단하기까지 기다린다. 오래된 자료의 10초 기본값과 혼동하면 안 된다. |
| `heartbeat.interval.ms` | `3000` (3초) | 기본값 사용 | Group Coordinator에게 Heartbeat를 보내는 간격이다. `session.timeout.ms`보다 작아야 하며 일반적으로 1/3 이하를 권장한다. |
| `max.poll.interval.ms` | `300000` (5분) | 기본값 사용 | 두 `poll()` 호출 사이에 허용되는 최대 시간이다. 처리 시간이 이를 넘으면 Consumer가 Group에서 이탈하고 Rebalance가 발생할 수 있다. |
| `max.poll.records` | `500` | 기본값 사용 | `poll()` 한 번이 애플리케이션에 반환하는 최대 Record 수다. Fetch 자체의 데이터 양을 제한하는 값은 아니다. |
| `group.instance.id` | `null` | 미설정 | 설정하면 Static Member가 되어 짧은 재시작 때문에 발생하는 Rebalance를 줄일 수 있다. Instance마다 고유해야 한다. |
| `partition.assignment.strategy` | `RangeAssignor`, `CooperativeStickyAssignor` | 기본값 사용 | Group 안에서 Partition을 나누는 전략 목록이다. 기본적으로 RangeAssignor가 먼저 사용된다. |

Classic Consumer Group에서는 Broker가 허용하는 Session Timeout 범위도 통과해야 한다.

| Broker 설정 | Kafka 3.8.1 기본값 | 역할 |
|---|---:|---|
| `group.min.session.timeout.ms` | `6000` (6초) | Consumer가 요청할 수 있는 최소 `session.timeout.ms`다. |
| `group.max.session.timeout.ms` | `1800000` (30분) | Consumer가 요청할 수 있는 최대 `session.timeout.ms`다. |

`session.timeout.ms`와 `max.poll.interval.ms`는 서로 다른 장애를 감시한다.

```text
Heartbeat 중단
→ session.timeout.ms 초과
→ Consumer 프로세스 또는 네트워크 장애로 판단

poll() 호출 지연
→ max.poll.interval.ms 초과
→ Consumer 처리 정체로 판단
```

Record 처리 시간이 길다면 무조건 `max.poll.interval.ms`부터 키우기보다 다음 순서로 본다.

```text
max.poll.records를 줄여 한 번의 처리량 감소
→ 긴 작업을 별도 Worker로 분리할지 검토
→ Consumer 처리 병렬성 또는 Partition 수 검토
→ 정상적으로 긴 작업일 때만 max.poll.interval.ms 조정
```

---

## 4.2 Consumer Fetch 설정

| 설정 | Kafka 3.8.1 기본값 | Plys 설정 | 역할과 주의점 |
|---|---:|---:|---|
| `fetch.min.bytes` | `1` Byte | 기본값 사용 | Broker가 Fetch 응답을 보내기 전에 모으려는 최소 데이터다. 크게 하면 요청 횟수는 줄지만 지연이 늘 수 있다. |
| `fetch.max.wait.ms` | `500` ms | 기본값 사용 | 최소 데이터가 모이지 않아도 응답하는 최대 대기 시간이다. |
| `max.partition.fetch.bytes` | `1048576` (1 MiB) | 기본값 사용 | Partition 하나당 반환받는 목표 최대 크기다. Consumer가 여러 Partition을 맡으면 합계 메모리는 더 커질 수 있다. |
| `fetch.max.bytes` | `52428800` (50 MiB) | 기본값 사용 | Fetch 응답 전체의 목표 최대 크기다. Consumer는 여러 Fetch를 병렬 수행할 수 있어 절대적인 전체 메모리 상한은 아니다. |
| `receive.buffer.bytes` | `65536` (64 KiB) | 기본값 사용 | Consumer Socket의 TCP 수신 버퍼 크기다. |
| `request.timeout.ms` | `30000` (30초) | 기본값 사용 | Consumer가 Broker 요청 응답을 기다리는 시간이다. |

Fetch는 대략 다음 조건 중 하나가 충족되면 응답한다.

```text
모인 데이터 >= fetch.min.bytes
또는
대기 시간 >= fetch.max.wait.ms
```

따라서 `fetch.min.bytes`를 높이고 `fetch.max.wait.ms`도 크게 잡으면 처리량은 좋아질 수 있지만 소량 메시지의 체감 지연이 커질 수 있다.

---

## 4.3 Consumer Offset과 Transaction 설정

| 설정 | Kafka 3.8.1 기본값 | Plys 설정 | 역할과 주의점 |
|---|---:|---:|---|
| `enable.auto.commit` | `true` | `false` | Offset 자동 Commit 여부다. Plys는 업무 처리 후 직접 ACK하기 위해 끈다. |
| `auto.commit.interval.ms` | `5000` (5초) | 사용하지 않음 | 자동 Commit이 켜져 있을 때 Commit하는 주기다. |
| `auto.offset.reset` | `latest` | `earliest` | 저장된 Offset이 없거나 삭제됐을 때 시작 위치다. 이미 유효한 Committed Offset이 있으면 적용되지 않는다. |
| `isolation.level` | `read_uncommitted` | 기본값 사용 | `read_committed`로 바꾸면 Kafka Transaction에서 Commit된 Record만 반환한다. 일반 DB Transaction과는 무관하다. |
| `default.api.timeout.ms` | `60000` (1분) | 기본값 사용 | 별도 Timeout을 주지 않은 Consumer API의 기본 제한 시간이다. |

Plys의 Spring Listener 설정도 Kafka Client 설정과 구분해야 한다.

| Spring Kafka 설정 | 일반 기본값 | Plys 설정 | 역할 |
|---|---:|---:|---|
| `spring.kafka.listener.ack-mode` | `BATCH` | `MANUAL` | Listener가 Offset Commit 시점을 어떻게 요청할지 정한다. Kafka Native Client의 설정이 아니라 Spring Kafka 설정이다. |
| `spring.kafka.listener.concurrency` | `1` | 기본값 사용 | Listener Container의 Consumer Thread 수다. Topic Partition 수보다 많아지면 쉬는 Consumer가 생긴다. |

`MANUAL`은 `acknowledge()` 호출과 동시에 무조건 Broker Commit이 끝난다는 뜻이 아니다. Container 처리 방식과 Commit API에 따라 실제 Commit 시점이 결정된다. 즉, “DB 작업 성공 뒤 ACK를 요청한다”는 정책으로 이해하는 것이 정확하다.

---

## 4.4 함께 조정해야 하는 설정

### Consumer가 처리 중 Group에서 빠질 때
- 처리 시간이 `max.poll.interval.ms`를 넘는지 먼저 확인한다. 한 번에 받는 양이 많다면 `max.poll.records`를 줄이고, 정상적으로 오래 걸리는 작업이라면 그다음 `max.poll.interval.ms`를 조정한다.

### Consumer 장애 감지를 빠르게 할 때
- `heartbeat.interval.ms`와 `session.timeout.ms`를 함께 본다. 너무 짧으면 일시적인 GC Pause나 네트워크 지연에도 Rebalance가 자주 발생할 수 있다.

### Fetch 처리량을 높일 때
- `fetch.min.bytes`를 높이면 Broker가 데이터를 더 모아 응답하므로 요청 횟수를 줄일 수 있다. 대신 `fetch.max.wait.ms`만큼 소량 메시지의 지연이 늘 수 있다.

### 큰 메시지를 보낼 때
- Producer의 `max.request.size`, Broker의 `message.max.bytes`, Topic의 `max.message.bytes`, Replica의 `replica.fetch.max.bytes`, Consumer의 `max.partition.fetch.bytes`를 함께 확인한다. 한쪽만 늘리면 발행·복제·소비 중 다른 단계에서 실패할 수 있다.

### 데이터 안전성을 높일 때
- 일반적으로 `replication.factor=3`, `min.insync.replicas=2`, Producer `acks=all`, `unclean.leader.election.enable=false`를 한 묶음으로 본다. 이 조합은 Broker 한 대 장애 중에도 안전한 쓰기를 허용하지만 ISR이 한 대만 남으면 가용성보다 일관성을 택해 쓰기를 거부한다.

### Producer 처리량을 높일 때
- `batch.size`와 `linger.ms`로 더 큰 Batch를 만들고 `compression.type`을 적용할 수 있다. 처리량만 보지 말고 추가 지연, CPU 사용량과 `buffer.memory` 사용량을 함께 측정해야 한다.

---

## 5. 메시지 처리 보장

### At-Most-Once
- Record를 최대 한 번 처리한다. 중복 가능성은 낮지만 처리 전에 Offset이 Commit되면 메시지가 유실될 수 있다.

### At-Least-Once
- Record를 한 번 이상 처리한다. 메시지 유실을 줄이는 대신 장애 시 중복 처리가 발생할 수 있다.

### Exactly-Once
- 재시도와 장애가 발생해도 결과가 논리적으로 한 번만 반영되는 처리 의미론이다. 적용 범위가 Kafka 내부인지 외부 DB까지 포함하는지 반드시 구분해야 한다.

### Idempotency
- 동일한 요청이나 메시지를 여러 번 처리해도 최종 결과가 한 번 처리한 것과 같게 유지되는 성질이다.

### Consumer Idempotence
- 같은 Record를 다시 소비해도 DB 결과가 중복되지 않도록 만드는 설계다.

대표적인 방법은 `eventId`와 처리 이력 테이블을 사용하는 것이다.

### Kafka Transaction
- 여러 Kafka Record 발행과 Consumer Offset Commit을 하나의 Kafka 트랜잭션으로 묶는 기능이다.

```
Topic A 소비
→ 가공
→ Topic B 발행
→ Topic A Offset Commit
```

Kafka 내부의 Read-Process-Write에는 유용하지만 외부 MySQL 트랜잭션까지 자동으로 하나로 묶지는 않는다.

### `read_committed`
- Consumer가 Kafka Transaction에서 Commit된 Record만 읽도록 하는 격리 수준이다.

### Atomicity
- 여러 작업이 전부 성공하거나 전부 실패해야 한다는 성질이다.

### DLT
- `Dead Letter Topic`의 약자다. 재시도해도 계속 실패하는 Record를 격리하는 Topic이다.

### Retry Topic
- 처리에 실패한 Record를 일정 시간 뒤 다시 처리하도록 전달하는 별도 Topic이다.

---

## 6. 시스템 간 트랜잭션 패턴

### Dual Write
- 하나의 요청에서 DB 저장과 Kafka 전송을 각각 수행하는 방식이다.

```
DB 저장 성공
→ Kafka 전송 실패
```

두 시스템이 하나의 트랜잭션을 공유하지 않으면 불일치가 발생할 수 있다.

### Transactional Outbox Pattern
- 업무 데이터와 발행할 이벤트를 같은 DB 트랜잭션으로 저장하는 패턴이다.

```
DB Transaction
├─ 업무 데이터 INSERT
└─ Outbox Event INSERT
```

이후 별도의 Relay 또는 CDC가 Outbox Event를 Kafka에 발행한다.

중요한 점은 **DB 저장과 Kafka 전송 자체를 한 트랜잭션으로 묶는 것이 아니라**, DB 안의 두 저장을 묶어 Dual Write 문제를 제거한다는 것이다.

Relay가 같은 이벤트를 여러 번 보낼 수 있으므로 Consumer Idempotence가 함께 필요하다.

### Inbox Pattern
- Consumer가 받은 `eventId`를 업무 데이터와 같은 DB 트랜잭션으로 기록하는 패턴이다.

```
eventId 저장 시도
→ 이미 존재하면 중복이므로 건너뜀
→ 처음이면 업무 데이터 반영
```

### Event ID
- 이벤트 한 건을 식별하는 고유 ID다. Producer 재전송이나 Consumer 재처리 시 중복을 판별하는 데 사용한다.

---

## 7. 데이터 변경 추적

### CDC
- `Change Data Capture`의 약자다. DB의 변경 로그를 읽어 `INSERT`, `UPDATE`, `DELETE`를 변경 이벤트로 변환하는 기술이다.

일반적으로 DB가 리스너에게 직접 Push하는 구조가 아니다.

```
애플리케이션이 DB 변경
→ MySQL이 Binlog 기록
→ CDC Connector가 Binlog 읽음
→ 변경 이벤트 생성
→ Kafka Topic 발행
```

### Binlog
- MySQL이 Commit된 데이터·스키마 변경을 순서대로 기록하는 Binary Log다. Replication과 시점 복구, CDC에 사용된다.

모든 `SELECT`나 일반 Query 기록이 아니라 DB 변경에 필요한 Event를 기록한다. Row, Statement, Mixed 형식이 존재한다. [[MySQL 공식 문서](https://dev.mysql.com/doc/refman/8.0/en/mysqlbinlog.html)](https://dev.mysql.com/doc/refman/8.0/en/mysqlbinlog.html)

### Kafka Connect
- Kafka와 외부 시스템 사이의 데이터를 이동하기 위한 실행 플랫폼이다. Source Connector와 Sink Connector를 배포·관리한다.

### Source Connector
- DB나 파일 시스템 등 외부 시스템의 데이터를 Kafka Topic으로 가져오는 Connector다.

### Sink Connector
- Kafka Topic의 Record를 Elasticsearch, DB, Object Storage 등 외부 시스템으로 내보내는 Connector다.

### Debezium
- MySQL 등의 Transaction Log를 읽어 변경 이벤트를 생성하는 대표적인 CDC Source Connector다.

Debezium MySQL Connector는 Binlog를 읽고 Row 단위의 `INSERT`, `UPDATE`, `DELETE` 이벤트를 Kafka Topic에 발행한다. 장애 복구 과정에서는 이벤트가 중복될 수 있으므로 수신 측 멱등성이 필요하다. [[Debezium 공식 문서](https://debezium.io/documentation/reference/stable/connectors/mysql.html)](https://debezium.io/documentation/reference/stable/connectors/mysql.html)

---

## 8. DB 정합성과 라우팅

### DB Transaction
- 여러 DB 작업을 하나의 단위로 묶어 모두 Commit하거나 Rollback하는 기능이다.

### `@Transactional`
- Spring에서 메서드의 DB 트랜잭션 경계를 지정하는 Annotation이다.

### Master DB
- 쓰기와 최신 데이터 조회를 담당하는 원본 DB다.

### Slave DB
- Master의 변경 사항을 복제해 주로 조회 트래픽을 담당하는 DB다.

### Read/Write Splitting
- 쓰기 요청은 Master, 일반 조회는 Slave로 나누는 구조다.

### Replication Lag
- Master에서 Commit된 변경이 Slave에 반영되기까지 발생하는 시간 차이다.

### Read-After-Write Consistency
- 쓰기 직후 조회했을 때 방금 작성한 데이터를 확인할 수 있어야 한다는 정합성 조건이다.

### RoutingDataSource
- 트랜잭션의 `readOnly` 여부 등에 따라 Master와 Slave DataSource를 선택하는 Spring 구성 요소다.

### ThreadLocal
- 값을 현재 Thread에만 저장하는 Java 기능이다. Kafka Consumer Thread에 저장한 값은 이후 사용자의 HTTP Request Thread와 공유되지 않는다.

---

## 9. Elasticsearch와 비교

### Elasticsearch Index
- 비슷한 JSON Document를 논리적으로 묶는 공간이다.

### Elasticsearch Shard
- Elasticsearch Index의 Document를 나누어 저장하는 물리적 처리 단위다. Shard 내부는 하나의 Lucene Index로 구현된다.

### Sharding
- Elasticsearch Index의 여러 Document를 여러 Primary Shard에 분배하는 것이다.

### Elasticsearch Replica Shard
- Primary Shard의 복사본이다.

### Kafka Partition과 Elasticsearch Shard
- 둘 다 분산 처리 단위라는 점은 비슷하지만 목적이 다르다.

```
Kafka Partition
→ 순서가 있는 Record Log
→ Producer·Consumer 병렬 처리 단위

Elasticsearch Shard
→ Document 검색 저장소
→ 색인·검색 분산 처리 단위
```

### Kafka와 Elasticsearch 복제 설정 차이
- Kafka와 Elasticsearch는 복제 설정 숫자의 의미가 다르다.

```
Kafka Replication Factor 3
= Leader 포함 총 3사본

Elasticsearch number_of_replicas=3
= Primary 1개 + Replica 3개
= 총 4사본
```

---

## 10. Plys에 실제 적용된 구성

### Kafka Cluster
- Kafka 3대가 모두 Broker와 Controller를 겸하는 Combined Mode다.

### Controller Quorum
- 세 Kafka Node 중 하나가 Active Controller, 나머지 두 개가 Standby Controller가 된다. 역할은 고정되지 않고 Raft 선거로 결정된다.

### Topic
- 다음 두 Topic을 사용한다.

```
plys.playlist.track-added
plys.playlist.track-removed
```

### Partition과 복제
- 각 Topic은 Partition 3개, Replication Factor 3으로 구성된다.

### Message Key
- `playlistUid`를 사용한다. 같은 Topic의 동일 Playlist 이벤트는 같은 Partition에 들어간다.

추가와 삭제는 서로 다른 Topic이므로 두 작업 사이의 순서는 보장되지 않는다.

### Producer 보장
- 다음 설정을 사용한다.

```
acks=all
enable.idempotence=true
retries=3
```

Producer 재전송 신뢰성은 고려했지만 API가 전송 Future를 기다리지 않아 HTTP 성공 시점에 Broker 저장 성공은 확정되지 않는다.

### Consumer 처리
- `plys-consumer-group`이 두 Topic을 소비하고 MySQL에 실제 추가·삭제를 반영한다.

### DB Transaction
- Consumer의 `@Transactional`은 Kafka Transaction이 아니라 MySQL/JPA Transaction이다.

### Offset 관리
- `enable-auto-commit=false`, `ack-mode=manual`을 사용한다. 다만 예외를 Consumer 내부에서 삼키고 있어 확정적인 재시도는 보장되지 않는다.

### 현재 보장 수준
- Plys는 다음 수준이다.

```
Kafka 비동기 처리
+ Producer 멱등성
+ DB Local Transaction
+ 수동 Offset 관리
```

다음 항목은 구현되지 않았다.

```
Kafka Transaction
Transactional Outbox
Inbox 기반 Consumer 멱등성
DLT와 명시적 재시도
DB Commit과 Offset Commit의 원자적 결합
```

따라서 Plys를 설명할 때는 **Exactly-Once를 구현했다고 말하면 안 되고**, “비동기 처리와 DB 로컬 트랜잭션, 수동 Offset 관리를 적용했으며 중복과 재시도 정책은 후속 보완 과제로 남았다”고 말하는 것이 정확하다.

---

# Spring Boot에서 Kafka 구현하기

## 필요한 파일

### 1. `build.gradle`
- Kafka Client와 Spring Kafka 기능을 사용하기 위한 의존성을 추가한다.

```gradle
implementation 'org.springframework.kafka:spring-kafka'
```

### 2. `application.properties`
- Broker 주소, 직렬화 방식, Consumer Group과 Offset Commit 정책을 설정한다.

```properties
spring.kafka.bootstrap-servers=kafka-1:9092,kafka-2:9092,kafka-3:9092

spring.kafka.producer.key-serializer=org.apache.kafka.common.serialization.StringSerializer
spring.kafka.producer.value-serializer=org.springframework.kafka.support.serializer.JsonSerializer

spring.kafka.consumer.group-id=plys-consumer-group
spring.kafka.consumer.key-deserializer=org.apache.kafka.common.serialization.StringDeserializer
spring.kafka.consumer.value-deserializer=org.springframework.kafka.support.serializer.JsonDeserializer
spring.kafka.consumer.enable-auto-commit=false

spring.kafka.listener.ack-mode=manual
```

다음은 Consumer 기본값을 명시하거나 튜닝할 때 사용하는 Spring Boot Property 이름이다. 기본값을 그대로 쓸 목적이라면 모두 적을 필요는 없다.

```properties
# Consumer 생존과 poll
spring.kafka.consumer.properties.session.timeout.ms=45000
spring.kafka.consumer.properties.heartbeat.interval.ms=3000
spring.kafka.consumer.properties.max.poll.interval.ms=300000
spring.kafka.consumer.max-poll-records=500

# Consumer fetch
spring.kafka.consumer.fetch-min-size=1
spring.kafka.consumer.fetch-max-wait=500ms
spring.kafka.consumer.properties.max.partition.fetch.bytes=1048576
spring.kafka.consumer.properties.fetch.max.bytes=52428800

# Offset와 Transaction Record 조회
spring.kafka.consumer.auto-offset-reset=earliest
spring.kafka.consumer.enable-auto-commit=false
spring.kafka.consumer.properties.isolation.level=read_uncommitted

# Spring Kafka Listener
spring.kafka.listener.ack-mode=manual
spring.kafka.listener.concurrency=1
```

Producer를 튜닝할 때는 다음 이름을 사용한다.

```properties
spring.kafka.producer.acks=all
spring.kafka.producer.retries=3
spring.kafka.producer.batch-size=16384
spring.kafka.producer.buffer-memory=33554432
spring.kafka.producer.compression-type=none
spring.kafka.producer.properties.enable.idempotence=true
spring.kafka.producer.properties.max.in.flight.requests.per.connection=5
spring.kafka.producer.properties.linger.ms=0
spring.kafka.producer.properties.delivery.timeout.ms=120000
spring.kafka.producer.properties.request.timeout.ms=30000
spring.kafka.producer.properties.max.block.ms=60000
spring.kafka.producer.properties.max.request.size=1048576
```

설정 이름을 적었다고 성능이 좋아지는 것은 아니다. Plys처럼 부하 테스트 시나리오와 측정 지표를 정한 뒤 한 번에 적은 수의 값만 바꾸고 같은 조건에서 비교해야 한다.

### 3. `KafkaConfig.java`
- 애플리케이션 실행 시 사용할 Topic을 자동 생성한다.

```java
@Configuration
public class KafkaConfig {

    @Bean
    public NewTopic trackAddedTopic() {
        return TopicBuilder
                .name("plys.playlist.track-added")
                .partitions(3)
                .replicas(3)
                .build();
    }
}
```

Broker에서 Topic을 미리 생성한다면 `NewTopic` Bean은 필수가 아니다.

### 4. `TrackEvent.java`
- Producer와 Consumer가 주고받을 Event의 데이터 형식을 정의한다.

```java
@Data
@Builder
@NoArgsConstructor
@AllArgsConstructor
public class TrackEvent {
    private String playlistUid;
    private String trackTitle;
    private String artist;
}
```

### 5. `TrackEventProducer.java`
- `KafkaTemplate`을 주입받아 Topic에 Event를 발행한다.

```java
@Component
@RequiredArgsConstructor
public class TrackEventProducer {

    private final KafkaTemplate<String, TrackEvent> kafkaTemplate;

    public void publish(TrackEvent event) {
        kafkaTemplate.send(
                "plys.playlist.track-added",
                event.getPlaylistUid(),
                event
        );
    }
}
```

### 6. `TrackEventConsumer.java`
- `@KafkaListener`로 Topic을 구독하고 수신한 Event를 처리한다.

```java
@Component
public class TrackEventConsumer {

    @KafkaListener(
        topics = "plys.playlist.track-added",
        groupId = "plys-consumer-group"
    )
    @Transactional
    public void consume(TrackEvent event, Acknowledgment ack) {
        // DB 작업
        ack.acknowledge();
    }
}
```

### 7. 기존 Service
- Producer를 주입받아 비즈니스 로직에서 Event 발행 메서드를 호출한다.

```java
@Service
@RequiredArgsConstructor
public class PlaylistService {

    private final TrackEventProducer producer;

    public void addTrack(...) {
        TrackEvent event = TrackEvent.builder()
                .playlistUid(playlistUid)
                .build();

        producer.publish(event);
    }
}
```

### 8. Kafka Broker 실행 파일
- Kafka를 직접 운영한다면 Docker Compose나 Broker 설정 파일이 필요하다. 외부 Managed Kafka를 사용한다면 접속 정보만 설정한다.

```text
docker-compose.kafka.yml
또는
server.properties
```

Plys의 Docker Compose에서는 Kafka Property를 대문자 환경 변수로 바꾸어 설정한다.

```yaml
KAFKA_PROCESS_ROLES: broker,controller
KAFKA_CONTROLLER_QUORUM_VOTERS: 1@plys-kafka-1:9093,2@plys-kafka-2:9093,3@plys-kafka-3:9093
KAFKA_NUM_PARTITIONS: 3
KAFKA_DEFAULT_REPLICATION_FACTOR: 3
KAFKA_MIN_INSYNC_REPLICAS: 2
KAFKA_LOG_RETENTION_HOURS: 168
KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR: 3
KAFKA_TRANSACTION_STATE_LOG_REPLICATION_FACTOR: 3
KAFKA_TRANSACTION_STATE_LOG_MIN_ISR: 2
```

대체로 `min.insync.replicas`는 `KAFKA_MIN_INSYNC_REPLICAS`처럼 점을 밑줄로 바꾸고 대문자로 표기한다. 다만 Docker Image마다 환경 변수 변환 규칙이 다를 수 있으므로 사용하는 Image 문서를 확인해야 한다.

## 주요 Annotation

- **`@Configuration`**: Kafka 설정 클래스로 등록한다.
- **`@Bean`**: `NewTopic` 같은 객체를 Spring Bean으로 등록한다.
- **`@Component`**: Producer와 Consumer를 Spring Bean으로 등록한다.
- **`@KafkaListener`**: 메서드가 지정한 Topic의 Record를 소비하게 한다.
- **`@Transactional`**: Consumer가 수행하는 DB 작업을 하나의 DB Transaction으로 묶는다.
- **`@RequiredArgsConstructor`**: `KafkaTemplate`, Repository와 Producer를 생성자로 주입한다.
- **`@EnableKafka`**: Spring Boot 자동 설정을 사용하면 일반적으로 직접 추가하지 않아도 된다.

## 주요 클래스와 메서드

- **`KafkaTemplate<K, V>`**: Spring에서 Kafka Record를 발행할 때 사용하는 핵심 Client다.
- **`kafkaTemplate.send(topic, key, value)`**: Topic에 Key와 Value를 비동기로 발행한다.
- **`CompletableFuture.whenComplete()`**: 비동기 발행의 성공 또는 실패 결과를 처리한다.
- **`@KafkaListener(topics, groupId)`**: 소비할 Topic과 Consumer Group을 지정한다.
- **`Acknowledgment.acknowledge()`**: Manual ACK 환경에서 Offset Commit을 요청한다.
- **`TopicBuilder.name()`**: 생성할 Topic 이름을 지정한다.
- **`partitions()`**: Topic의 Partition 수를 지정한다.
- **`replicas()`**: Topic Partition의 Replication Factor를 지정한다.

## 필수 여부

- **필수**: Kafka 의존성, Broker 접속 설정, Producer 또는 Consumer 구현.
- **상황별 필요**: Event DTO, Topic 생성 Config, Manual ACK, DB Transaction.
- **Broker 직접 운영 시 필요**: Docker Compose 또는 Kafka Server 설정.

## 전체 흐름

```text
build.gradle
→ Kafka 의존성 추가

application.properties
→ Broker·Producer·Consumer 설정

KafkaConfig
→ Topic 생성

TrackEvent
→ Event 형식 정의

TrackEventProducer
→ KafkaTemplate.send()

TrackEventConsumer
→ @KafkaListener로 소비

PlaylistService
→ Producer 호출
```

Plys 기준 핵심 구성은 **Kafka 설정, Event DTO, Producer, Consumer, 기존 Service 연결**이다.
