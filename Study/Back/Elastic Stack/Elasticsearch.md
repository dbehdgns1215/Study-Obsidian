
# Elasticsearch 시스템 구조

Elasticsearch 노드들은 클라이언트와 통신하기 위한 http 포트 (`9200 ~ 9299`), 노드 간의 데이터 교환을 위한 tcp 포트 (`9300 ~ 9399`) 이렇게 총 2개의 포트를 열어두고 있음.

일반적으로 1개의 물리 서버마다 하나의 노드를 실행하는 것을 권장.

> Elasticsearch는, 기본적으로 서버 메모리의 절반 정도를 힙 메모리로 할당해주고 남은 OS의 메모리를 OS 페이지 캐시로 사용할 수 있게끔 할당해주는 것이 권장 설정.

![[Pasted image 20260811210007.png]]
- 이때, 각 노드는 별개의 서버이기에 hostname은 다름. 따라서 포트 중복 가능.

- 그런데 만약 아래와 같다면?
![[Pasted image 20260811210129.png]]
- 하나의 서버에 2개의 노드가 있다면 포트 번호는 중복될 수 없음

# 클러스터

또한, 하나의 클러스터로 묶여있으면 데이터 교환이 일어날 수 있지만, 별개의 클러스터라면 데이터 교환이 일어나지 않음.
- 데이터 교환이 가능하다 -> 노드 A와 노드 B가 하나의 클러스터에 묶여있을 때, 노드 A에 저장된 데이터는 노드 B가 접근 가능. 역도 성립.

각 클러스터는 반드시 하나의 **마스터 노드**를 가져야만 함.
또한 마스터 후보 노드는 여러개가 존재할 수 있음. Kafka처럼 고가용성을 위한 설계


## 디스커버리

노드가 처음 실행될 때 같은 서버 또는 `discovery.seed_hosts: [ ]`에 설정된 네트워크 상의 다른 노드들을 찾아 하나의 클러스터로 **바인딩**하는 과정을 **디스커버리**라고 함.
- 노드 1과 노드 2가 하나의 클러스터, 노드 3는 다른 클러스터라고 하고 이 3개의 노드가 하나의 물리 서버에서 실행된다고 가정했을 때, 노드 3가 처음 실행되면 같은 서버의 노드 1 노드 2를 발견해도 클러스터명이 달라서 handshake가 실패하게 됨. 이후에는 노드 3이 스스로 마스터 노드로 선출되게 됨.

### 디스커버리 과정

![[Pasted image 20260811210850.png]]

> 클러스터에 노드가 무수히 많아도 보통 `discovery.seed_hosts` 설정에는 처음에 탐색할 노드 3~5 개 정도만 설정 하면 큰 문제 없이 클러스터가 바인딩 됨.
> 
> 보통은 마스터 후보 노드들을 지정하게 되며 처음 탐색하는 대상 노드는 반드시 먼저 가동이 되고 있어야 함.


## 인덱스와 샤드
- 단일 데이터 단위 도큐먼트(**document**)
- 도큐먼트의 집합 인덱스(**Index**) 또는 인디시즈(**Indices**)
- 인덱스는 기본적으로 샤드(**shard**)라는 단위로 분리되고 각 노드에 분산되어 저장됨.
	- 샤드는 루씬의 단일 검색 인스턴스

![[Pasted image 20260811235019.png]]

> 데이터의 논리 구조
> Cluster
> 	└─ Index
> 	    └─ Shard
> 		    └─ Document

> 데이터의 실제 실행/배치 구조
> Cluster 
> 	└─ Node
> 		└─ Shard Copy
> 			└─ Lucene Index
> 				└─ Segment
> 					└─ Document

인덱스를 생성할 때 별도의 설정을 하지 않으면 7.0 버전부터는 기본 1개의 샤드로 인덱스가 생성됨.
또 클러스터에 노드를 추가하게 되면 샤드들이 각 노드들로 분산되고 기본으로 1개의 복제본을 생성하게 됨.

처음 생성된 샤드를 **프라이머리 샤드**, 복제본은 **레플리카 샤드**라 부름

![[Pasted image 20260811235029.png]]
- 그림을 보면, 각 Node마다 Shard들이 저장되어 있는데 하늘색이 Primary Shard, 회색이 Replica Shard.
- 1번 Shard의 경우 Node-2에 Primary Shard가 있고, Node-4에 Replica Shard가 존재함.
- 즉, `number_of_replicas: 1`로 설정되어 각 Primary Shard마다 Replica가 1개씩 존재하며, 하나의 Shard는 총 2개의 Shard Copy를 가지는 구조.

> 노드가 1개만 있는 경우, 프라이머리 샤드만 존재하고 복제본은 생성되지 않음.
> 또 Elasticsearch는 아무리 작은 클러스터라도 데이터 가용성과 무결성을 위해 최소 3개의 노드로 구성할 것을 권장하고 있음.

또한 같은 샤드와 복제본은 동일한 데이터를 담고 있으며 반드시 서로 다른 노드에 저장이 되어야 함.

만약 장애가 발생해서 프라이머리 샤드가 유실된 경우에는 새로 프라이머리 샤드를 생성하게 되는 것이 아니라, 남아있던 복제본이 먼저 프라이머리 샤드로 승격되고 다른 노드에 새롭게 복제본을 생성하게 됨.
마찬가지로 복제본이 유실되면 프라이머리 샤드가 다른 노드에 새롭게 복제본을 생성하게 됨.
단, 이때는 기본값 1분으로 설정된 타임아웃이 존재함. 복제본의 경우에는 서버 재부팅이나 Elasticsearch 재시작 등의 이유로 정상적으로 돌아올 수 있기 때문에 1분의 유예 시간을 주는 것. 물론 이건 설정값으로 설정 가능. `index.unassigned.node_left.delayed_timeout`


> 장애를 판별하는 기준은, 마스터 노드가 다른 노드들에게 장애 감지용 신호를 1초 간격으로 보내고, 이를 최대 10초의 타임아웃까지 기다려주며 3번 연속 실패할 경우에는 해당 노드를 장애로 판단해 클러스터에서 제거하게 됨.
> 응답이 느린 것을 떠나 TCP 연결 자체가 끊어졌다면 즉시 장애 노드로 처리함.


## 샤드 개수 설정

샤드의 개수는 인덱스를 처음 생성할 때만 지정할 수 있음. 인덱스를 재색인 하지 않는 이상 바꿀 수 없음.

물론 복제본의 개수는 나중에 변경이 가능.

## 마스터 노드와 데이터 노드

클러스터는 하나 이상의 노드로 이루어지고 이 중 하나의 노드는 인덱스의 메타 데이터, 샤드의 위치와 같은 클러스터 상태 정보를 관리하는 마스터 노드의 역할을 수행하게 됨. 클러스터마다 하나의 마스터 노드가 존재하며 마스터 노드의 역할을 수행할 수 있는 노드가 없다면 클러스터는 작동이 정지됨.

기본적으로는 모든 노드가 마스터 노드로 선출될 수 있는 Master Eligible Node임. 이 마스터 후보 노드들은 기본적으로 처음부터 마스터 노드가 가지는 정보들을 공유하고 있기 때문에 즉시 마스터로 승격이 가능함.

단, 클러스터가 커져서 노드와 샤드들의 개수가 많아지게 되면 모든 노드들이 마스터 노드의 정보를 계속 공유하는 것이 부담이 될 수 있음.


데이터 노드는 실제로 색인된 데이터를 저장하고 있는 노드임.

> 마스터 후보 노드를 하나만 놓게되면 해당 마스터 노드가 유실되었을 때 클러스터 전체가 마비될 위험이 있음.
> 따라서 최소한의 백업용 마스터 노드를 설정하게 되는데, 이때 마스터 후보 노드들은 3개 이상의 **홀수** 개를 놓는 것을 권장하고 있음.

이와 관련해, 마스터 후보 노드가 최소 n개 이상 존재하고 있을 때만 클러스터가 동작하게 해야하고 그렇지 않은 경우는 클러스터 동작을 멈추도록 설정해야 함.
`discovery.zen.minimum_master_nodes: n`
- 만약 그렇지 않을 때, 마스터 후보 노드가 짝수 개이면 데이터 정합성에 Split Brain 이라는 문제가 생길 가능성이 커짐.


# Elasticsearch 데이터 처리
모든 정보는 `json`으로 통한다.



## REST API - CRUD

기본 구조
```bash
Index: my_index

Document
_id = 1
{
  "name": "Jongmin Kim",
  "message": "안녕하세요 Elasticsearch"
}
```
- 해당 문서에 접근하는 주소는
	- `my_index/_doc/1`

```text
my_index  → Index 이름
_doc      → 문서 API 경로에 들어가는 고정 문자열
1         → Document의 _id
```

중요한게, 예전에는 Mapping Type 이라고 해서 인덱스와 \_id 사이에 문서를 구별하는 식별자 같은 느낌으로 경로가 하나 더 있었음.

하지만 8.0 버전부터 사라졌으며 지금은 관례상 \_doc 라는 내용으로 자리를 지키고 있는 중.

> 있는게 가독성이 더 좋아보이는데 왜 사라졌을까?
> 
> 기본적으로 Elasticsearch는 Lucene을 기반으로 Wrapping 한 형태를 띄고 있음.
> 따라서 Lucene의 데이터 처리 방식과 연관이 있음.
> 
> 만약 company 라는 인덱스가 있다고 가정해보자.
> 이 인덱스에는 employee의 타입(테이블의 개념)과 department의 타입이 존재하고 있고, 이들이 가지고 있는 필드(열, 또는 키)들은 서로 독립적일 것이라고 당연하게 생각이 됨.
> 하지만 실제 Lucene에서 처리할 때는 타입 구분이 무시되고 같은 필드로 처리되는 상황.
> 
> 즉,
> 1. 독립된 두 타입에 이름이 같은 필드가 있으면, 두 필드는 무조건 '동일한 데이터 타입(예: 둘 다 text)'이어야만 하는 충돌 문제가 발생함. (한쪽은 text, 한쪽은 integer로 선언 불가능)
> 
> 2. 내부적으로는 타입 구분을 위해 문서마다 `_type` 필드를 몰래 추가해 검색하는 편법을 썼기 때문에, 데이터가 섞여서 저장되는 '희소성(Sparsity) 문제'가 발생하여 디스크와 메모리(OS 페이지 캐시) 효율이 극도로 떨어짐.
>    
> 결론적으로, 매핑 타입은 멀티 테이블처럼 보이기 위한 ES의 '가짜 껍데기'였을 뿐이며, Lucene의 물리적 구조(인덱스-필드)와 1대1로 매칭되지 않아 성능 저하와 혼란을 야기했기 때문에 8.0에서 완전히 퇴출당함. 지금은 1 인덱스 = 1 테이블 구조가 강제됨.

| 우리가 부르는 말  | 엑셀(Excel) 기준  | 관계형 DB(RDBMS) 기준  | 엘라스틱서치(ES) 기준            | 진짜 의미                      |
| ---------- | ------------- | ----------------- | ------------------------ | -------------------------- |
| **행 / 로우** | 가로 1줄         | 레코드 (Record) / 튜플 | 문서 (Document)            | **데이터 1건**                 |
| **열 / 컬럼** | 세로 1줄         | 필드 (Field)        | **필드 (Field)**           | **데이터 항목의 이름 (Key)**       |
| **자료형**    | 셀 서식 (텍스트/숫자) | 데이터 타입            | **필드 타입 (Field Type)**   | **글자냐, 숫자냐, 날짜냐**          |
| **매핑 타입**  | (굳이 치면 시트 이름) | 테이블 (Table)       | **매핑 타입 (Mapping Type)** | 옛날에 쓰던 **가짜 분류 이름표 (폐기됨)** |
아무튼 결국, 성격이 완전히 다른 데이터라면 인덱스 자체를 나누는 방식을 택하면 됨.


| 목적               | 메서드      | 예시                    |
| ---------------- | -------- | --------------------- |
| 문서 생성/전체 덮어쓰기    | `PUT`    | `PUT test/_doc/1`     |
| ID 자동 생성해서 문서 생성 | `POST`   | `POST test/_doc`      |
| 문서 조회            | `GET`    | `GET test/_doc/1`     |
| 문서 일부 수정         | `POST`   | `POST test/_update/1` |
| 문서 삭제            | `DELETE` | `DELETE test/_doc/1`  |

### Create

도큐먼트 id를 직접 지정해서 데이터를 입력할 때는 PUT 메서드를 이용함.

#### 입력
```javascript
PUT my_index/_doc/1
{
  "name":"유동훈",
  "message":"엘라스틱서치 완전정복 렛츠고"
}
```

#### 출력
```javascript
{
  "_index" : "my_index",
  "_id" : "1",
  "_version" : 1,
  "result" : "created",
  "_shards" : {
    "total" : 2,
    "successful" : 2,
    "failed" : 0
  },
  "_seq_no" : 0,
  "_primary_term" : 1
}
```

- `result`가 `created`로 표시가 되고 있는데 동일한 URL에 다른 내용의 도큐먼트를 다시 입력하면 기존 도큐먼트의 전체 내용이 새로운 내용으로 덮어씌워지게 됨. 그리고 `created`가 아닌 `updated`가 표시됨.
    - 내부적으로는 기존 도큐먼트를 삭제된 상태로 표시하고 새로운 도큐먼트를 다시 색인하는 방식으로 처리됨.
- 또한 `_doc` 대신 `_create`를 사용하면 새로운 도큐먼트의 입력만 허용하는 것이 가능해짐.
    - 즉, 이미 존재하는 도큐먼트 id일 경우에는 오류가 나고 그렇지 않으면 `created` 되는 것.
- 도큐먼트 id를 직접 지정하지 않고 Elasticsearch가 자동으로 생성하게 하고 싶다면 `POST my_index/_doc` 형태로 입력할 수도 있음.

#### Read

#### 입력
```javascript
GET my_index/_doc/1
```

#### 출력
```javascript
{
  "_index" : "my_index",
  "_id" : "1",
  "_version" : 1,
  "_seq_no" : 0,
  "_primary_term" : 1,
  "found" : true,
  "_source" : {
    "name" : "유동훈",
    "message" : "엘라스틱서치 완전정복 렛츠고"
  }
}
```
- `found`는 해당 id의 도큐먼트가 존재하는지를 나타냄.
- `_source`에는 실제로 입력했던 도큐먼트의 내용이 들어있음.

#### Update

일부 필드를 바꾸고자 전체 도큐먼트 내용을 매번 다시 입력하는 것은 번거롭기에 이때 사용하는 것이 바로 `_update`.

`_update`에서는 수정할 내용을 `doc` 안에 넣어주면 됨.

#### 입력
```javascript
POST my_index/_update/1
{
  "doc": {
    "message":"엘라스틱썻치 완전 정복 레레츠고고"
  }
}
```

### 출력
```javascript
{
  "_index" : "my_index",
  "_id" : "1",
  "_version" : 2,
  "result" : "updated",
  "_shards" : {
    "total" : 2,
    "successful" : 2,
    "failed" : 0
  },
  "_seq_no" : 1,
  "_primary_term" : 1
}
```

기존 도큐먼트가

```javascript
{
  "name":"유동훈",
  "message":"엘라스틱서치 완전정복 렛츠고"
}
```

였다면 `message` 필드만 변경했기 때문에 결과적으로

```javascript
{
  "name":"유동훈",
  "message":"엘라스틱썻치 완전 정복 레레츠고고"
}
```

가 됨.

즉 `_update`를 사용하면 사용자는 수정하려는 필드만 전달할 수 있음.

다만 내부적으로 해당 필드만 직접 수정하는 것은 아니고, 기존 도큐먼트를 가져와 변경 내용을 적용한 뒤 변경된 도큐먼트를 다시 색인하는 방식으로 동작함.

참고로 실제로 도큐먼트가 수정되면 `_version` 값도 증가하게 됨.

### Delete

#### 입력
```javascript
DELETE my_index/_doc/1
```

#### 출력
```javascript
{
  "_index" : "my_index",
  "_id" : "1",
  "_version" : 3,
  "result" : "deleted",
  "_shards" : {
    "total" : 2,
    "successful" : 2,
    "failed" : 0
  },
  "_seq_no" : 2,
  "_primary_term" : 1
}
```
- `result`가 `deleted`로 표시되며 해당 id의 도큐먼트가 삭제됨.
- 도큐먼트를 삭제하는 것 역시 하나의 쓰기 작업이기 때문에 `_version` 값이 증가함.



## \_bulk API

### Elasticsearch Bulk API 핵심

- 일반 방식  
    `PUT`, `POST`, `DELETE` 같은 REST API 요청을 문서마다 따로 보냄.

```text
PUT /test/_doc/1
PUT /test/_doc/2
DELETE /test/_doc/3
POST /test/_update/4
```
→ HTTP 요청 4번

- Bulk 방식  
    `POST /_bulk` 요청 **한 번**에 여러 작업을 같이 넣음.

```text
POST /_bulk

index  → 문서 저장
create → 새 문서 생성
update → 문서 수정
delete → 문서 삭제
```
→ HTTP 요청 1번  
→ 실제 문서 작업은 여전히 4개

### 왜 쓰냐

**작업 개수를 줄이는 게 아니라, 네트워크 요청 횟수와 HTTP 처리 오버헤드를 줄이려고 사용함.**

```text
일반 API
작업 1000개 → HTTP 요청 1000번

Bulk
작업 1000개 → 예: 한 번에 100개씩 → HTTP 요청 10번
```

### 가장 중요한 구분

```text
PUT / POST / GET / DELETE
= HTTP 메서드

index / create / update / delete
= Bulk 요청 안에서 각 문서에 어떤 작업을 할지 나타내는 Bulk Action
```


**Bulk API = 여러 Elasticsearch 문서 작업을 큰 HTTP 요청 하나에 묶어서 전송하는 대량 처리용 API.**


## \_search API

검색은 인덱스 단위로 이루어진다. `GET <인덱스명>/_search` 형식으로 사용하며 쿼리를 입력하지 않으면 전체 도큐먼트를 찾는 **match_all** 검색을 수행함.

특정 인덱스에서 **"name"** 이라는 값을 검색하기 위해서는 다음과 같이 입력한다.

#### 입력

```
GET <인덱스명>/_search?q=name
```

#### 출력

```json
{
  "took" : 3,
  "timed_out" : false,
  "_shards" : {
    "total" : 1,
    "successful" : 1,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : {
      "value" : 2,
      "relation" : "eq"
    },
    "max_score" : 0.105360515,
    "hits" : [
      {
        "_index" : "test",
        "_type" : "_doc",
        "_id" : "3",
        "_score" : 0.105360515,
        "_source" : {
          "field" : "value three"
        }
      },
      {
        "_index" : "인덱스명",
        "_type" : "_doc",
        "_id" : "1",
        "_score" : 0.105360515,
        "_source" : {
          "field" : "value two"
        }
      }
    ]
  }
}
```
- `hits.total.value` 부분에 검색 결과의 문서 전체 개수가 표시되고 더 나아가 "hits" 라는 배열 안에 정확도가 높은 문서가 표시됨. 이때 정확도를 **relevancy**라고 함.

만약, 검색어가 2개라면 **AND** 조건을 사용해서 검색하면 됨. 그렇게 하면 두 값이 모두 들어간 문서만 검색되게 됨. (`AND`, `OR`, `NOT` 모두 사용 가능)

```
GET <인덱스명>/_search?q=name AND phoneNum
```

또 다른 검색 방식으로는 데이터 본문 검색이 있음.

검색 쿼리를 데이터 본문, Data Body로 입력하는 방식으로 Elasticsearch의 QueryDSL을 사용하며 쿼리 또한 json 형식으로 되어있음.

주로 사용되는 `match` 쿼리의 경우 다음과 같음

```
GET test/_search
{
  "query": {
    "match": {
      "field": "name"
    }
  }
}
```
- field 값이 name인 도큐먼트를 검색하는 쿼리.
- 데이터 본문 방식으로 쿼리를 입력할 때는 무조건 `query` 지정자로 시작해야 함.


## 멀티테넌시

Elasticsearch는 여러 개의 인덱스를 한꺼번에 묶어서 검색할 수 있는 멀티테넌시를 지원함.
즉, `logs-2026-08-01`과 `logs-2026-08-02`와 같이 날짜별로 있는 인덱스들을 `logs-*/_search` 명령으로 한꺼번에 검색이 가능하다는 뜻.

시계열 로그 데이터를 다룰 때는 인덱스를 일단위로 구분하는 것이 좋음.

여러 인덱스를 한꺼번에 검색하는 다른 방식으로는

```
GET logs-2026-08-01,2026-08-02,2026-08-03/_search
```
- 쉼표를 이용해 검색하는 방식

```
GET logs-2026-*/_search
```
- 와일드 카드를 이용해 검색하는 방식

이렇게 2가지가 존재함.







# 검색과 쿼리 - Full Text Query


### match

`match` 쿼리는 풀 텍스트 검색에 사용되는 가장 일반적인 쿼리로, 특정 인덱스의 `message` 필드에 특정 단어가 포함되어 있는 모든 문서를 검색함.
- 사실 특정 인덱스의 특정 필드명을 사용하지만, 현재 가이드북에서 예제 데이터가 `message` 라는 필드명을 쓰고 있어서 그걸 그대로 따르는 것.

단, 여러 개의 검색어를 집어넣으면 `OR` 조건으로 검색됨.

만약,

```json
GET my_index/_search
{
  "query": {
    "match": {
      "message": "quick dog"
    }
  }
}
```
- 이런 쿼리가 있었다면, quick이 들어간 도큐먼트와 dog가 들어간 도큐먼트 모두가 검색되는 것.
	- 이게 만약 싫고 `AND`로 검색하고 싶다면?
```json
GET my_index/_search
{
  "query": {
    "match": {
      "message": {
        "query": "quick dog",
        "operator": "and"
      }
    }
  }
}
```
- `operator` 추가
	- 만약, "quick dog" 이 구문과 정확히 일치하는 문서가 필요하다면?
```json
GET my_index/_search
{
  "query": {
    "match_phrase": {
      "message": "quick dog"
    }
  }
}
```
- `match_phrase`를 사용해주면 됨.
	- 근데 "quick"와 "dog" 사이에 무언가가 들어간 값을 검색하고 싶다면?
```json
GET my_index/_search
{
  "query": {
    "match_phrase": {
      "message": {
        "query": "quick dog",
        "slop": 1
      }
    }
  }
}
```
- `slop` 옵션의 값을 1로 주고 검색하면 됨. -> 즉 "quick jumping dog" 같은 도큐먼트가 검색됨.

### query_string

결국 URL의 q 파라미터를 사용하게 된다면 루씬의 검색 문법을 본문 검색에도 사용할 수 있음. 

```json
GET my_index/_search
{
  "query": {
    "query_string": {
      "default_field": "message",
      "query": "(jumping AND lazy) OR \"quick dog\""
    }
  }
}
```
 - `match_phrase` 처럼 구문 검색을 할 때는 `\"` 안에 넣어주면 됨.


## Bool 복합 쿼리 - Bool Query

Bool Query의 인자는 다음 4가지임.
- `must`: 쿼리가 참인 도큐먼트들을 검색
- `must_not`: 쿼리가 거짓인 도큐먼트들을 검색
- `should`: 검색 결과 중 이 쿼리에 해당하는 도큐먼트의 점수를 높임
- `filter`: 쿼리가 참인 도큐먼트를 검색하지만 스코어를 계산하지 않음.
	- `must` 보다 검색 속도가 빠르고 **캐싱**이 가능함

```json
GET <인덱스명>/_search
{
  "query": {
    "bool": {
      "must": [
        { <쿼리> }, …
      ],
      "must_not": [
        { <쿼리> }, …
      ],
      "should": [
        { <쿼리> }, …
      ],
      "filter": [
        { <쿼리> }, …
      ]
    }
  }
}
```


## 정확도 - Relevancy

RDBMS 같은 시스템에서는 쿼리 조건에 부합하는지만 판단하여 결과를 가져올 뿐, 각 결과들이 얼마나 정확한지에 대한 판단은 보통 불가능함.

하지만 Elasticsearch와 같은 FTS 검색 엔진은 검색 결과가 입력된 검색 조건과 얼마나 정확하게 일치하는 지를 계산하는 알고리즘을 가지고 있음. (`BM25`)

### 스코어 점수

이 점수는 검색된 결과가 얼마나 검색 조건과 일치하는 지를 나타내며 점수가 높은 순으로 결과를 보여줌.


### should

특정 도큐먼트의 가중치를 줘서 정확도를 올리고 싶을 때 사용하면 됨.

예를 들어서

match 쿼리로 fox를 퐇마하는 도큐먼트를 검색했을 때,

#### 입력
```json
GET my_index/_search
{
  "query": {
    "match": {
      "message": "fox"
    }
  }
}
```

#### 출력
```json
{
  "took" : 1,
  "timed_out" : false,
  "_shards" : {
    "total" : 1,
    "successful" : 1,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : {
      "value" : 4,
      "relation" : "eq"
    },
    "max_score" : 0.32951736,
    "hits" : [
      {
        "_index" : "my_index",
        "_type" : "_doc",
        "_id" : "1",
        "_score" : 0.32951736,
        "_source" : {
          "message" : "The quick brown fox"
        }
      },
      {
        "_index" : "my_index",
        "_type" : "_doc",
        "_id" : "4",
        "_score" : 0.32951736,
        "_source" : {
          "message" : "Brown fox brown dog"
        }
      },
      {
        "_index" : "my_index",
        "_type" : "_doc",
        "_id" : "2",
        "_score" : 0.23470737,
        "_source" : {
          "message" : "The quick brown fox jumps over the lazy dog"
        }
      },
      {
        "_index" : "my_index",
        "_type" : "_doc",
        "_id" : "3",
        "_score" : 0.23470737,
        "_source" : {
          "message" : "The quick brown fox jumps over the quick dog"
        }
      }
    ]
  }
}
```
- `lazy`가 포함된 결과에 가중치를 줘서 상위로 올리고 싶으면

#### 입력
```json
GET my_index/_search
{
  "query": {
    "bool": {
      "must": [
        {
          "match": {
            "message": "fox"
          }
        }
      ],
      "should": [
        {
          "match": {
            "message": "lazy"
          }
        }
      ]
    }
  }
}
```

#### 출력
```json
{
  "took" : 1,
  "timed_out" : false,
  "_shards" : {
    "total" : 1,
    "successful" : 1,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : {
      "value" : 4,
      "relation" : "eq"
    },
    "max_score" : 0.9489644,
    "hits" : [
      {
        "_index" : "my_index",
        "_type" : "_doc",
        "_id" : "2",
        "_score" : 0.9489644,
        "_source" : {
          "message" : "The quick brown fox jumps over the lazy dog"
        }
      },
      {
        "_index" : "my_index",
        "_type" : "_doc",
        "_id" : "1",
        "_score" : 0.32951736,
        "_source" : {
          "message" : "The quick brown fox"
        }
      },
      {
        "_index" : "my_index",
        "_type" : "_doc",
        "_id" : "4",
        "_score" : 0.32951736,
        "_source" : {
          "message" : "Brown fox brown dog"
        }
      },
      {
        "_index" : "my_index",
        "_type" : "_doc",
        "_id" : "3",
        "_score" : 0.23470737,
        "_source" : {
          "message" : "The quick brown fox jumps over the quick dog"
        }
      }
    ]
  }
}
```
- 이전과 비교했을 때, 바뀐 순서를 보면 `lazy`가 들어간 `fox` 가 정확도 1등

이걸 그러면 어떻게 사용할 수 있을까?

`커피 주전자`을 검색한다고 가정해보자.
- 먼저 `match` 쿼리로 `커피`와 `주전자`을 모두 검색한 뒤, `should`를 통해 `match_phrase``커피 주전자`로 검색하게 된다면, 커피와 관련된 용품, 주전자와 관련된 용품들이 검색되고 최상단에는 `커피 주전자` 가 올라가게 되는 것.
	- 또한 여기서 `slop`을 주게 되면 `커피 온도조절 주전자` 와 같이 특정 단어가 중간에 낀 결과에도 가중치를 부여해서 상단에 띄우는 응용도 가능.

```json
{
  "query": {
    "bool": {
      "should": [
        { 
          "match": { 
            "message": { 
              "query": "커피 주전자", 
              "operator": "or", 
              "boost": 1 
            } 
          } 
        },
        { 
          "match_phrase": { 
            "message": { 
              "query": "커피 주전자", 
              "boost": 5 
            } 
          } 
        },
        { 
          "match_phrase": { 
            "message": { 
              "query": "커피 주전자", 
              "slop": 2, 
              "boost": 3 
            } 
          } 
        }
      ],
      "minimum_should_match": 1 
    }
  }
}
```

## 정확값 쿼리 - Exact Value Query

지금까지의 FTS 검색은 스코어 점수 기반의 정확도가 높은 결과를 가져왔었지만 이외에도 검색 조건의 참/거짓 여부만 판별해서 결과를 가져오는 쿼리도 존재함.

이를 `정확값(Exact Value)`라고 하는데 말 그대로 일치 여부를 따지는 검색.

다음 3개의 쿼리를 보자.

```json
GET my_index/_search
{
  "query": {
    "match": {
      "message": "fox"
    }
  }
}
```

```json
GET my_index/_search
{
  "query": {
    "bool": {
      "must": [
        {
          "match": {
            "message": "fox"
          }
        },
        {
          "match": {
            "message": "quick"
          }
        }
      ]
    }
  }
}
```

```json
GET my_index/_search
{
  "query": {
    "bool": {
      "must": [
        {
          "match": {
            "message": "fox"
          }
        }
      ],
      "filter": [
        {
          "match": {
            "message": "quick"
          }
        }
      ]
    }
  }
}
```

차이가 무엇일까?
- 첫 번째 쿼리는 `match` 단독으로 fox를 검색하고 그 안에서 `fox`라는 검색어의 스코어를 BM25 알고리즘으로 계산할 것.
- 두 번쨰 쿼리는 `fox`도 들어가고 `quick`도 들어가는 문서를 추려내는 것. 그리고 `fox`, `quick` 두 단어 모두의 빈도수(TF)와 희귀도(IDF)를 끌어모아 합산한 점수
- 세 번째 쿼리는 결과만 놓고 보면 `fox`, `quick`가 모두 들어가는 문서가 맞지만 두 번째 쿼리와의 차이점은 `quick`가 `filter` 안에 있기 때문에 `Yes/No` 판정에만 사용하고 점수를 매기지는 않는다는 것.

따라서 `match`를 써야할 때는 사용자가 검색창에 친 키워드들을 더 정확히 정교하게 줄세워야 할 때 즉, 스코어링해서 결과를 보여줘야 할 때이고

`filter`를 써야할 때는 `가격 1만원 이하`, `"brand: 스타벅스"`, `재고 있음` 등과 같은 `조건`이 필요할 때 사용하는 것. 이러한 조건은 결국 검색 관련성 점수를 높여주지 않기 때문에 특정 조건으로 결과를 **거르는 것**이 목적인 것.
```json
{
  "query": {
    "bool": {
      "filter": [
        { "term": { "status": "PUBLISHED" } },
        { "range": { "created_at": { "gte": "2026-01-01" } } },
        { "terms": { "category_id": [101, 102] } }
      ]
    }
  }
}
```
- 이런 느낌으로 `bool` 안에 `filter`를 넣어서 여러 `조건`들로 필터링하는 것임.


참고로 `filter` 내부에 `must_not`과 같은 다른 `bool 쿼리`를 넣으려면 `filter` 내부에 `bool` 쿼리를 먼저 넣고 그 안에 다시 `must_not`을 넣어야 함.

```json
GET my_index/_search
{
  "query": {
    "bool": {
      "must": [
        {
          "match": {
            "message": "fox"
          }
        }
      ],
      "filter": [
        {
          "bool": {
            "must_not": [
              {
                "match": {
                  "message": "dog"
                }
              }
            ]
          }
        }
      ]
    }
  }
}
```
- 위 커리를 보면 `bool` -> `must` -> `match` 이렇게 있고 또 `bool` -> `filter` -> `bool` -> `must_not` -> `match` 이렇게 존재하는 것을 볼 수 있다.

> **`bool`** (최상위 통과 게이트 오픈)
> 
> **`filter`** (여기는 점수 계산 안 하고 비트맵 캐시만 태우는 구역이야!)
> 
> **`bool`** (그 필터 구역 안에서 다시 복합 논리를 짜기 위해 껍데기로 여는 2차 게이트)
> 
> **`must_not`** (그 안에서 "이 조건은 무조건 제외해라"라는 부정 연산자 선언)
> 
> **`match`** ("제외할 대상의 검색어가 바로 'dog'야"라고 지정하는 실제 검색 쿼리 부품)


```json
{
  "query": {
    "bool": {
      "must": [ { "match": { "message": "fox" } } ],
      "must_not": [ { "match": { "message": "dog" } } ]
    }
  }
}
```
- 사실상 이게 직관적인데 왜 그렇게 하지 않을까?
- 사실상 같은 결과가 나옴, "`fox` 찾을건데 `dog` 안들어갔으면 좋겠다"
	- 성능상의 차이가 발생함.
		- `must_not`은 이름만 `not`일 뿐, Elastcsearch 내부 엔진에서는 스코어링 컨텍스트의 테두리 안에서 처리됨. 즉, 엔진은 이 `must_not` 조건을 점수를 내진 않지만 쿼리 전체의 최적화 흐름과 가중치 계산 파이프라인에 편입시켜야하는 조건으로 인식하는 것.
		- 이로 인해 JVVM 힙 메모리의 영구 Roaring Bitmap 캐시 영역에 안착하지 못하고 쿼리가 들어올 때마다 CPU 연산 파이프라인을 매번타게 돼서 성능상의 손해를 보게되는 샘.



### keyword

문자열 데이터는 `keyword` 형식으로 저장하여 정확값 검색이 가능함.

```json
GET my_index/_search
{
  "query": {
    "bool": {
      "filter": [
        {
          "match": {
            "message.keyword": "Brown fox brown dog"
          }
        }
      ]
    }
  }
}
```
- `"message.keyword"`를 통해서 `Brownm fox brown dog` 문지열과 공백, 대소문자까지 정확히 일치하는 데이터만을 결과로 리턴하게 됨.
	- `keyword` 타입으로 저장된 필드는 스코어를 계산하지 않고 정확값의 일치 여부만을 따지기에 스코어는 항상 `0.0`으로 나오게 됨. 따라서 스코어를 계산하지 않는 `keyword` 값을 검색할 때는 `filter` 구문 안에 넣도록 하자.
























# 참고 자료
https://esbook.kimjmin.net/03-cluster/3.1-cluster-settings