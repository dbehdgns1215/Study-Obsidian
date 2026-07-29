
## 1. 시스템 인프라 아키텍처

### Kafka Cluster

같은 클러스터로 묶인 Broker와 Controller의 집합이다. Topic과 Partition을 분산 저장하고 장애가 발생하면 Leader를 재선출한다.

### Broker

Kafka Record를 실제 디스크에 저장하고 Producer·Consumer의 요청을 처리하는 Kafka 서버 프로세스다.

### Bootstrap Server

클라이언트가 Kafka Cluster에 처음 접속할 때 사용하는 Broker 주소 목록이다. 모든 Broker를 적을 필요는 없지만 일부 장애를 고려해 여러 주소를 지정한다.

```
Bootstrap Broker 접속
→ Cluster Metadata 조회
→ Partition Leader 확인
→ 실제 Leader Broker와 통신
```

### Cluster Metadata

Broker, Topic, Partition, Leader, Replica, ISR 등 Kafka Cluster의 현재 구조를 나타내는 정보다.

---

## 1.1 메타데이터 관리 시스템

### ZooKeeper

과거 Kafka 외부에서 Broker 등록, Controller 선출과 일부 클러스터 메타데이터 관리를 담당하던 분산 코디네이터다. Record 자체는 ZooKeeper가 아니라 Kafka Broker에 저장됐다.

### KRaft

ZooKeeper 없이 Kafka 내부의 Controller Quorum과 Raft 기반 Metadata Log로 클러스터 상태를 관리하는 방식이다.

### Metadata Log

Controller들이 Broker·Topic·Partition 상태의 변경 이력을 순서대로 기록하고 복제하는 내부 로그다.

---

## 1.2 클러스터 통제 엔진

### Controller

Broker 등록, Partition Leader 선출, Replica 배치 등 클러스터의 메타데이터를 관리하는 Kafka 역할이다.

### Controller Quorum

KRaft Metadata Log를 복제하고 Active Controller를 선출하는 Controller들의 집합이다.

### Active Controller

Controller Quorum의 현재 Leader다. 메타데이터 변경을 주도하고 Broker 장애가 발생하면 필요한 Partition Leader 선출을 조율한다.

### Standby Controller

Active Controller의 Metadata Log를 복제하며 대기하는 Controller다. Active 장애 시 새로운 Active 후보가 된다.

### Raft 합의 알고리즘

Controller들이 동일한 Metadata Log 상태를 유지하고 과반수 투표로 Active Controller를 선출하는 원리다. Leader 선출뿐 아니라 로그 복제와 Commit 여부도 관리한다.

### Quorum

합의를 성립시키는 데 필요한 과반수다.

```
Controller 3대 → 최소 2대 필요 → 1대 장애 허용
Controller 5대 → 최소 3대 필요 → 2대 장애 허용
```

### Combined Mode

하나의 Kafka 프로세스가 Broker와 Controller를 동시에 담당하는 구성이다.

```
process.roles=broker,controller
```

Plys의 Kafka 3대는 모두 Combined Mode다. 세 노드 중 하나가 Active Controller, 나머지가 Standby Controller가 된다.

### Dedicated Controller

Broker 역할 없이 Controller만 담당하는 Kafka Node다. 중요 운영 환경에서는 Broker 부하와 Controller를 격리하고 독립적으로 확장하기 위해 사용한다.

### `node.id`

KRaft Cluster에서 Kafka Node를 구분하는 고유 번호다.

### `controller.quorum.voters`

Controller 선거에 참여하는 Node ID와 주소를 지정하는 설정이다.

```
1@kafka-1:9093,2@kafka-2:9093,3@kafka-3:9093
```

### Control Plane

Controller가 Metadata, Broker 상태와 Leader 선출을 관리하는 경로다.

### Data Plane

Producer의 Record가 Partition Leader에 저장되고 Consumer에게 전달되는 실제 데이터 경로다.

---

## 2. 데이터 저장 구조

### Topic

Record를 업무 종류별로 분류하는 논리적 공간이다. Cluster 아래에서 데이터를 구분하는 가장 큰 논리 단위다.

### Record

Kafka가 저장하고 전달하는 메시지 한 건이다.

```
Key + Value + Timestamp + Headers
```

### Partition

Topic의 Record를 나누어 저장하는 Append-only 로그이자 병렬 처리 단위다. Kafka의 순서는 Topic 전체가 아니라 Partition 내부에서만 보장된다.

```
Topic
├─ Partition 0: A → C → F
├─ Partition 1: B → E
└─ Partition 2: D → G
```

Record 하나를 여러 Partition으로 쪼개는 것이 아니라, Record 전체가 특정 Partition 하나에 저장된다.

### Segment

Partition의 로그를 일정 크기나 시간 단위로 나눈 실제 파일 묶음이다. Partition 하나가 영원히 커지는 파일 하나로 저장되는 것은 아니다.

### Offset

Partition 안에서 Record의 위치를 나타내는 번호다. Partition마다 0부터 독립적으로 증가한다.

```
Partition 0: Offset 0, 1, 2
Partition 1: Offset 0, 1, 2
```

### Retention

Record를 Kafka에 얼마나 오래 보관할지 정하는 정책이다. Consumer가 읽었다고 Record가 즉시 삭제되지는 않는다.

---

## 2.1 고가용성과 복제

### Partition Leader

해당 Partition의 일반적인 읽기와 쓰기를 담당하는 Broker의 Partition 복제본이다.

### Partition Follower

Leader의 Record를 Fetch해 복제하는 Partition 복제본이다. 정상적으로 동기화된 Follower는 Leader 장애 시 승격 후보가 된다.

### Replication Factor

Leader를 포함해 동일 Partition을 총 몇 개의 복제본으로 보관할지 나타내는 값이다.

```
Replication Factor 3
= Leader 1개 + Follower 2개
= 총 3사본
```

### ISR

`In-Sync Replicas`의 약자다. 설정된 허용 지연 범위 안에서 Leader를 따라가고 있는 Replica 집합이다.

100% 같은 Offset이어야만 ISR인 것은 아니다. 일정 시간 이상 Leader를 따라오지 못하면 ISR에서 제외된다.

### `min.insync.replicas`

`acks=all`을 사용하는 Producer의 쓰기를 허용하기 위해 필요한 최소 ISR 수다. Leader도 ISR 수에 포함된다.

```
Replication Factor = 3
min.insync.replicas = 2
```

ISR이 2개 이상이면 쓰기를 허용하지만, 1개만 남으면 데이터 안전성을 위해 쓰기를 거부한다.

### Unclean Leader Election

ISR이 모두 사라졌을 때 ISR 밖의 Replica를 Leader로 승격하는 선택이다. 가용성은 높일 수 있지만 복제되지 않은 Record를 잃을 수 있다.

---

## 3. Producer 데이터 송신

### Producer

Record를 생성해 Topic의 Partition Leader에게 전송하는 Kafka Client다.

### Message Key

Record와 함께 전송되는 값으로, 기본 Partitioner가 Partition을 결정할 때 사용한다.

고유한 값일 필요는 없다. 중요한 성질은 **같은 Key가 일반적으로 같은 Partition으로 들어간다**는 점이다.

```
playlistUid="A" → Partition 1
playlistUid="A" → Partition 1
```

Partition 수를 변경하면 기존과 다른 Partition이 선택될 수 있다.

### Serializer

Java 객체를 Kafka가 네트워크로 전송할 수 있는 Byte Array로 변환한다.

```
String → StringSerializer
TrackEvent → JsonSerializer
```

### Partitioner

Topic, Key와 Cluster Metadata를 바탕으로 Record를 보낼 Partition을 선택하는 Producer 구성 요소다.

### Record Accumulator

Producer가 전송할 Record를 Partition별 Batch로 모아 두는 메모리 버퍼다.

### Batch

같은 Partition으로 보낼 여러 Record를 묶은 전송 단위다. Batch로 보내면 네트워크 요청 횟수와 오버헤드를 줄일 수 있다.

### `batch.size`

Partition별 Batch가 사용할 목표 최대 크기를 지정한다. 이 크기를 채우지 않아도 `linger.ms`가 지나면 전송할 수 있다.

### `linger.ms`

Batch를 더 채우기 위해 Producer가 기다릴 수 있는 최대 시간이다.

```
작게 설정 → 낮은 지연, 작은 Batch
크게 설정 → 높은 처리량, 추가 지연 가능
```

### Sender Thread

Record Accumulator의 Batch를 가져와 Partition Leader에게 네트워크 요청을 보내는 Producer의 백그라운드 Thread다.

### `acks`

Producer가 Record 전송을 성공으로 판단하기 위해 기다릴 Broker 확인 수준이다.

```
acks=0   → Broker 응답을 기다리지 않음
acks=1   → Leader 저장 확인
acks=all → 현재 ISR의 저장 확인
```

### Retry

일시적인 네트워크 오류나 Leader 변경이 발생했을 때 Producer가 Record를 다시 보내는 동작이다.

### Callback

비동기 전송이 성공하거나 실패했을 때 실행되는 코드다. Plys에서는 `CompletableFuture.whenComplete()`를 사용한다.

### Producer Idempotence

Producer 재시도로 같은 Record가 Broker에 중복 기록되는 일을 줄이는 기능이다.

```
enable.idempotence=true
```

Producer ID와 Sequence Number를 이용한다. Consumer의 DB 중복 저장까지 막아 주지는 않는다.

---

## 4. Consumer 데이터 수신

### Consumer

Topic의 Partition Leader에서 Record를 Fetch하고 업무 로직을 수행하는 Kafka Client다.

### Consumer Group

하나의 목적을 위해 Topic의 Partition을 나누어 처리하는 Consumer들의 집합이다.

### Partition 독점 규칙

동일한 Consumer Group 안에서는 Partition 하나를 동시에 Consumer 한 명만 담당한다.

```
Partition 3개 + Consumer 2개
Consumer A → Partition 0, 1
Consumer B → Partition 2
```

Consumer가 Partition보다 많으면 남는 Consumer는 아무 작업도 하지 않는다.

### Group Coordinator

Consumer Group의 가입, Heartbeat, Offset Commit과 Rebalance를 조율하는 Broker다.

### Rebalance

Consumer가 추가·제거되거나 Partition 수가 변할 때 Partition 담당자를 다시 배정하는 과정이다.

### Committed Offset

Consumer Group이 처리를 완료했다고 Kafka에 기록한 위치다. 일반적으로 **마지막 처리 Record가 아니라 다음에 읽을 Offset**을 의미한다.

```
Offset 7까지 처리 완료
→ Committed Offset 8
```

### `__consumer_offsets`

Consumer Group의 Committed Offset과 Group Metadata를 저장하는 Kafka 내부 Topic이다.

### Auto Commit

Kafka Client가 일정 주기로 Offset을 자동 Commit하는 방식이다. 업무 처리가 끝나기 전에 Commit될 위험이 있다.

### Manual ACK

업무 처리가 끝난 뒤 애플리케이션이 직접 `acknowledge()`를 호출해 Offset Commit을 요청하는 방식이다.

### Consumer Lag

Partition의 최신 Offset과 Consumer Group의 Committed Offset 차이다.

```
Latest Offset 1,000
Committed Offset 700
Consumer Lag 300
```

Lag이 증가한다는 것은 Consumer 처리가 Producer의 유입 속도를 따라가지 못한다는 뜻이다.

### `auto.offset.reset`

Consumer Group에 저장된 Offset이 없을 때 어디서부터 읽을지 정한다.

```
earliest → 가장 오래된 보존 Record부터
latest   → 새로 들어오는 Record부터
```

---

## 5. 메시지 처리 보장

### At-Most-Once

Record를 최대 한 번 처리한다. 중복 가능성은 낮지만 처리 전에 Offset이 Commit되면 메시지가 유실될 수 있다.

### At-Least-Once

Record를 한 번 이상 처리한다. 메시지 유실을 줄이는 대신 장애 시 중복 처리가 발생할 수 있다.

### Exactly-Once

재시도와 장애가 발생해도 결과가 논리적으로 한 번만 반영되는 처리 의미론이다. 적용 범위가 Kafka 내부인지 외부 DB까지 포함하는지 반드시 구분해야 한다.

### Idempotency

동일한 요청이나 메시지를 여러 번 처리해도 최종 결과가 한 번 처리한 것과 같게 유지되는 성질이다.

### Consumer Idempotence

같은 Record를 다시 소비해도 DB 결과가 중복되지 않도록 만드는 설계다.

대표적인 방법은 `eventId`와 처리 이력 테이블을 사용하는 것이다.

### Kafka Transaction

여러 Kafka Record 발행과 Consumer Offset Commit을 하나의 Kafka 트랜잭션으로 묶는 기능이다.

```
Topic A 소비
→ 가공
→ Topic B 발행
→ Topic A Offset Commit
```

Kafka 내부의 Read-Process-Write에는 유용하지만 외부 MySQL 트랜잭션까지 자동으로 하나로 묶지는 않는다.

### `read_committed`

Consumer가 Kafka Transaction에서 Commit된 Record만 읽도록 하는 격리 수준이다.

### Atomicity

여러 작업이 전부 성공하거나 전부 실패해야 한다는 성질이다.

### DLT

`Dead Letter Topic`의 약자다. 재시도해도 계속 실패하는 Record를 격리하는 Topic이다.

### Retry Topic

처리에 실패한 Record를 일정 시간 뒤 다시 처리하도록 전달하는 별도 Topic이다.

---

## 6. 시스템 간 트랜잭션 패턴

### Dual Write

하나의 요청에서 DB 저장과 Kafka 전송을 각각 수행하는 방식이다.

```
DB 저장 성공
→ Kafka 전송 실패
```

두 시스템이 하나의 트랜잭션을 공유하지 않으면 불일치가 발생할 수 있다.

### Transactional Outbox Pattern

업무 데이터와 발행할 이벤트를 같은 DB 트랜잭션으로 저장하는 패턴이다.

```
DB Transaction
├─ 업무 데이터 INSERT
└─ Outbox Event INSERT
```

이후 별도의 Relay 또는 CDC가 Outbox Event를 Kafka에 발행한다.

중요한 점은 **DB 저장과 Kafka 전송 자체를 한 트랜잭션으로 묶는 것이 아니라**, DB 안의 두 저장을 묶어 Dual Write 문제를 제거한다는 것이다.

Relay가 같은 이벤트를 여러 번 보낼 수 있으므로 Consumer Idempotence가 함께 필요하다.

### Inbox Pattern

Consumer가 받은 `eventId`를 업무 데이터와 같은 DB 트랜잭션으로 기록하는 패턴이다.

```
eventId 저장 시도
→ 이미 존재하면 중복이므로 건너뜀
→ 처음이면 업무 데이터 반영
```

### Event ID

이벤트 한 건을 식별하는 고유 ID다. Producer 재전송이나 Consumer 재처리 시 중복을 판별하는 데 사용한다.

---

## 7. 데이터 변경 추적

### CDC

`Change Data Capture`의 약자다. DB의 변경 로그를 읽어 `INSERT`, `UPDATE`, `DELETE`를 변경 이벤트로 변환하는 기술이다.

일반적으로 DB가 리스너에게 직접 Push하는 구조가 아니다.

```
애플리케이션이 DB 변경
→ MySQL이 Binlog 기록
→ CDC Connector가 Binlog 읽음
→ 변경 이벤트 생성
→ Kafka Topic 발행
```

### Binlog

MySQL이 Commit된 데이터·스키마 변경을 순서대로 기록하는 Binary Log다. Replication과 시점 복구, CDC에 사용된다.

모든 `SELECT`나 일반 Query 기록이 아니라 DB 변경에 필요한 Event를 기록한다. Row, Statement, Mixed 형식이 존재한다. [MySQL 공식 문서](https://dev.mysql.com/doc/refman/8.0/en/mysqlbinlog.html)

### Kafka Connect

Kafka와 외부 시스템 사이의 데이터를 이동하기 위한 실행 플랫폼이다. Source Connector와 Sink Connector를 배포·관리한다.

### Source Connector

DB나 파일 시스템 등 외부 시스템의 데이터를 Kafka Topic으로 가져오는 Connector다.

### Sink Connector

Kafka Topic의 Record를 Elasticsearch, DB, Object Storage 등 외부 시스템으로 내보내는 Connector다.

### Debezium

MySQL 등의 Transaction Log를 읽어 변경 이벤트를 생성하는 대표적인 CDC Source Connector다.

Debezium MySQL Connector는 Binlog를 읽고 Row 단위의 `INSERT`, `UPDATE`, `DELETE` 이벤트를 Kafka Topic에 발행한다. 장애 복구 과정에서는 이벤트가 중복될 수 있으므로 수신 측 멱등성이 필요하다. [Debezium 공식 문서](https://debezium.io/documentation/reference/stable/connectors/mysql.html)

---

## 8. DB 정합성과 라우팅

### DB Transaction

여러 DB 작업을 하나의 단위로 묶어 모두 Commit하거나 Rollback하는 기능이다.

### `@Transactional`

Spring에서 메서드의 DB 트랜잭션 경계를 지정하는 Annotation이다.

### Master DB

쓰기와 최신 데이터 조회를 담당하는 원본 DB다.

### Slave DB

Master의 변경 사항을 복제해 주로 조회 트래픽을 담당하는 DB다.

### Read/Write Splitting

쓰기 요청은 Master, 일반 조회는 Slave로 나누는 구조다.

### Replication Lag

Master에서 Commit된 변경이 Slave에 반영되기까지 발생하는 시간 차이다.

### Read-After-Write Consistency

쓰기 직후 조회했을 때 방금 작성한 데이터를 확인할 수 있어야 한다는 정합성 조건이다.

### RoutingDataSource

트랜잭션의 `readOnly` 여부 등에 따라 Master와 Slave DataSource를 선택하는 Spring 구성 요소다.

### ThreadLocal

값을 현재 Thread에만 저장하는 Java 기능이다. Kafka Consumer Thread에 저장한 값은 이후 사용자의 HTTP Request Thread와 공유되지 않는다.

---

## 9. Elasticsearch와 비교

### Elasticsearch Index

비슷한 JSON Document를 논리적으로 묶는 공간이다.

### Elasticsearch Shard

Elasticsearch Index의 Document를 나누어 저장하는 물리적 처리 단위다. Shard 내부는 하나의 Lucene Index로 구현된다.

### Sharding

Elasticsearch Index의 여러 Document를 여러 Primary Shard에 분배하는 것이다.

### Elasticsearch Replica Shard

Primary Shard의 복사본이다.

### Kafka Partition과 Elasticsearch Shard

둘 다 분산 처리 단위라는 점은 비슷하지만 목적이 다르다.

```
Kafka Partition
→ 순서가 있는 Record Log
→ Producer·Consumer 병렬 처리 단위

Elasticsearch Shard
→ Document 검색 저장소
→ 색인·검색 분산 처리 단위
```

### Kafka와 Elasticsearch 복제 설정 차이

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

Kafka 3대가 모두 Broker와 Controller를 겸하는 Combined Mode다.

### Controller Quorum

세 Kafka Node 중 하나가 Active Controller, 나머지 두 개가 Standby Controller가 된다. 역할은 고정되지 않고 Raft 선거로 결정된다.

### Topic

다음 두 Topic을 사용한다.

```
plys.playlist.track-added
plys.playlist.track-removed
```

### Partition과 복제

각 Topic은 Partition 3개, Replication Factor 3으로 구성된다.

### Message Key

`playlistUid`를 사용한다. 같은 Topic의 동일 Playlist 이벤트는 같은 Partition에 들어간다.

추가와 삭제는 서로 다른 Topic이므로 두 작업 사이의 순서는 보장되지 않는다.

### Producer 보장

다음 설정을 사용한다.

```
acks=all
enable.idempotence=true
retries=3
```

Producer 재전송 신뢰성은 고려했지만 API가 전송 Future를 기다리지 않아 HTTP 성공 시점에 Broker 저장 성공은 확정되지 않는다.

### Consumer 처리

`plys-consumer-group`이 두 Topic을 소비하고 MySQL에 실제 추가·삭제를 반영한다.

### DB Transaction

Consumer의 `@Transactional`은 Kafka Transaction이 아니라 MySQL/JPA Transaction이다.

### Offset 관리

`enable-auto-commit=false`, `ack-mode=manual`을 사용한다. 다만 예외를 Consumer 내부에서 삼키고 있어 확정적인 재시도는 보장되지 않는다.

### 현재 보장 수준

Plys는 다음 수준이다.

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