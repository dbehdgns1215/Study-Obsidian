# Cluster와 Node
## Cluster
- 여러 Elasticsearch Node가 하나의 시스템처럼 동작하도록 묶인 단위.

## Node
- 실행 중인 Elasticsearch 인스턴스 하나.

## Master Node
- Cluster 상태, Node 참여/이탈, Index 생성/삭제, Shard 배치 등을 관리하는 Node.

## Master-eligible Node
- Master로 선출될 자격을 가진 Node.

## Data Node
- 실제 Shard를 저장하고 검색, 색인, 수정, 삭제, Aggregation 등을 수행하는 Node.

## Ingest Node
- Document를 저장하기 전에 파싱, Field 가공, 데이터 변환 등을 수행하는 Node.

## Coordinating Node
- 검색 요청을 여러 Shard에 나눠 보내고 결과를 모아 최종 결과를 만드는 역할을 하는 Node.

## Node Role
- 해당 Node가 어떤 기능을 수행할 수 있는지 지정하는 설정. `master`, `data`, `ingest` 등이 있음.

## Node Attribute
- Node에 사용자가 임의로 붙이는 추가 속성. Rack, Availability Zone 등의 정보를 표시할 때 사용.

---
# Index와 Document
## Index
- 관련된 Document들을 묶어 관리하는 논리적인 데이터 단위. 내부적으로 여러 Shard로 나뉨.

## Document
- Elasticsearch에 저장되는 데이터 한 건. 일반적으로 JSON 형태.

## Field
- Document를 구성하는 각각의 데이터 항목.

## Mapping
- Index 내부 Field의 이름, 자료형, 검색 방식 등을 정의하는 구조.

## Field Type
- `text`, `keyword`, `integer`, `date` 등 Field의 데이터 형식을 나타내는 Type.

## Mapping Type
- 과거 하나의 Index 안에서 Document를 종류별로 나누던 중간 계층. 현재는 제거됨.

## `_source`
- Elasticsearch에 입력했던 원본 JSON Document를 보관하는 영역.

---
# Shard
## Shard
- 하나의 Elasticsearch Index를 실제 저장과 처리를 위해 나눈 조각.
- Shard 하나는 사실상 하나의 Lucene Index.

## Primary Shard
- Document가 최초로 저장되는 원본 Shard.

## Replica Shard
- Primary Shard의 복사본.
- 장애 대응과 검색 부하 분산에 사용됨.

## Shard Copy
- Primary Shard 또는 Replica Shard 하나를 통틀어 부르는 표현.

## Unassigned Shard
- 존재해야 하지만 현재 어느 Node에도 배치되지 못한 Shard.

## Routing
- 특정 Document를 어느 Primary Shard에 저장할지 결정하는 과정.

---
# Shard 배치와 이동
## Shard Allocation
- 특정 Shard Copy를 어느 Data Node에 둘지 결정하는 것.

## Shard Relocation
- 이미 한 Node에 있는 Shard를 다른 Node로 옮기는 것.

## Shard Recovery
- 다른 Shard에서 데이터를 복사해 새로운 Shard Copy를 정상 상태로 만드는 과정.

## Rebalancing
- 특정 Node에 Shard가 몰리지 않도록 여러 Node 사이의 Shard 분포를 다시 맞추는 것.

## Allocation Awareness
- Rack이나 Availability Zone 같은 장애 영역을 고려해서 Primary Shard와 Replica Shard를 분산 배치하는 기능.

## Forced Awareness
- 특정 장애 영역이 사라져도 남은 영역에 Replica Shard를 무조건 몰아서 만들지 않도록 제한하는 기능.

---
# 물리 인프라와 장애 영역
## Rack
- 데이터센터에서 여러 물리 서버를 장착하는 서버 캐비닛.
- Rack 단위로 전원이나 네트워크 장애가 발생할 수 있음.

## Availability Zone
- 클라우드 환경에서 전원, 네트워크 등이 독립적으로 구성된 장애 영역.

## 장애 영역
- 하나의 장애가 동시에 영향을 줄 수 있는 물리적 또는 논리적 범위.
- Rack, Availability Zone, 데이터센터 등이 해당할 수 있음.

---
# Lucene 내부 구조
## Lucene
- Elasticsearch 내부에서 실제 색인과 검색을 수행하는 검색 라이브러리.

## Lucene Index
- Lucene이 Document와 검색용 자료구조를 저장하는 단위.
- Elasticsearch의 Shard 하나가 사실상 하나의 Lucene Index.

## Segment
- Lucene Index를 구성하는 더 작은 저장 단위.
- 하나의 Lucene Index 안에 여러 Segment가 존재할 수 있음.

## Segment Merge
- 여러 개의 작은 Segment를 더 큰 Segment로 합치는 작업.

## Inverted Index
- `단어 → 해당 단어를 가진 Document` 형태로 저장해 빠른 검색을 가능하게 하는 자료구조.

## Doc Values
- `Document → 값` 형태로 저장하는 컬럼 기반 자료구조.
- 정렬과 Aggregation 등에 주로 사용됨.

## Stored Fields
- 검색 후 실제 Field 값을 다시 가져오기 위해 Lucene에 별도로 저장하는 데이터.

---
# 텍스트 검색
## Analyzer
- 문자열을 검색 가능한 형태로 가공하는 전체 처리 과정.

## Token
- Analyzer를 거친 뒤 만들어지는 검색의 기본 단위.

## Tokenizer
- 문자열을 여러 Token으로 나누는 역할.

## Token Filter
- 만들어진 Token을 소문자화하거나 불용어를 제거하는 등 추가 가공하는 역할.

## `text`
- 문장을 분석한 뒤 Full-text Search에 사용하는 문자열 타입.

## `keyword`
- 문자열 전체를 하나의 값으로 취급하는 타입.
- Exact Match, 정렬, Aggregation 등에 주로 사용.

## Full-text Search
- 문장을 분석한 뒤 단어 단위로 관련 Document를 찾는 검색 방식.

## Exact Match
- 문자열 전체 값이 정확하게 일치하는지를 확인하는 검색 방식.

## Relevance Score
- 검색어와 Document가 얼마나 관련 있는지를 나타내는 점수.

---
# 검색 처리
## Search Request
- Elasticsearch에 특정 조건의 Document를 찾도록 보내는 요청.

## Distributed Search
- 여러 Shard에서 동시에 검색한 뒤 결과를 합쳐 최종 결과를 만드는 방식.

## Scatter
- Coordinating Node가 검색 요청을 여러 관련 Shard로 나누어 보내는 과정.

## Gather
- 여러 Shard에서 받은 검색 결과를 Coordinating Node가 모아서 합치는 과정.

## Aggregation
- 데이터를 그룹화하거나 개수, 평균, 합계 등을 계산하는 기능.

## Query DSL
- Elasticsearch 검색 조건을 JSON 형태로 표현하는 검색 문법.

---
# Data Tier
## Data Tier
- 데이터의 사용 빈도와 보관 기간에 따라 저장 Node를 구분하는 구조.

## Hot Tier
- 최근 생성되고 읽기와 쓰기가 자주 발생하는 데이터를 저장하는 Tier.

## Warm Tier
- 시간이 지나 쓰기는 줄었지만 검색은 여전히 필요한 데이터를 저장하는 Tier.

## Cold Tier
- 접근 빈도가 낮은 오래된 데이터를 상대적으로 저렴하게 보관하는 Tier.

## Frozen Tier
- 거의 사용하지 않는 장기 데이터를 Searchable Snapshot 등을 이용해 저비용으로 보관하는 Tier.

## Content Tier
- 상품, 문서, 기사처럼 시간이 지나도 검색 가치가 크게 변하지 않는 데이터를 저장하는 Tier.

## Index Lifecycle Management (ILM)
- 시간이나 조건에 따라 Index를 Hot → Warm → Cold → 삭제 등의 단계로 자동 관리하는 기능.

---
# Cluster 구성
## Discovery
- Elasticsearch Node가 다른 Node를 찾아 같은 Cluster에 참여하는 과정.

## `discovery.seed_hosts`
- 새로운 Node가 Cluster를 찾을 때 처음 접속해볼 Master-eligible Node 주소 목록.

## `cluster.initial_master_nodes`
- 완전히 새로운 Cluster를 최초 생성할 때 첫 Master 선거에 참여할 Node를 지정하는 설정.

## Cluster State
- 현재 Node, Index, Mapping, Shard 위치 등 Cluster 전체의 상태 정보.

## Green 상태
- 모든 Primary Shard와 Replica Shard가 정상적으로 배치된 상태.

## Yellow 상태
- 모든 Primary Shard는 정상이나 일부 Replica Shard가 배치되지 않은 상태.

## Red 상태
- 하나 이상의 Primary Shard가 배치되지 않아 일부 데이터에 접근할 수 없는 상태.

---
# 저장과 색인
## Refresh
- 새로 색인된 데이터를 검색 가능한 Segment에 반영하는 과정.

## Refresh Interval
- 자동으로 Refresh가 수행되는 주기.

## Near Real-Time Search
- Document를 저장한 즉시가 아니라 Refresh 이후 검색 가능해지는 Elasticsearch의 특성.

## Translog
- 아직 Lucene에 완전히 안전하게 반영되지 않은 변경 내용을 장애 복구를 위해 기록하는 Transaction Log.

## Flush
- Translog 상태를 정리하고 Lucene의 안전한 저장 지점을 만드는 과정.

## Lucene Commit
- 현재 Lucene Segment 상태를 디스크에 안전한 Commit 지점으로 기록하는 작업.

## Soft Deletes
- Document를 즉시 물리 삭제하지 않고 삭제 표시를 남긴 뒤 이후 Segment Merge 과정에서 실제 제거하는 방식.

---
# 디스크 관리
## Disk Watermark
- Node의 디스크 사용량에 따라 Shard Allocation과 Relocation을 제어하는 기준.

## Low Watermark
- 디스크 사용량이 높아져 새로운 Shard를 해당 Node에 배치하지 않기 시작하는 기준.

## High Watermark
- 디스크 사용량이 더 높아져 기존 Shard를 다른 Node로 이동시키기 시작하는 기준.

## Flood Stage
- 디스크 공간이 거의 소진되어 데이터 보호를 위해 Index 쓰기를 제한할 수 있는 단계.

---
# 통신
## HTTP Port
- 애플리케이션이나 사용자가 Elasticsearch REST API에 접근할 때 사용하는 Port.
- 일반적으로 `9200`.

## Transport Port
- Elasticsearch Node끼리 내부 통신할 때 사용하는 Port.
- 일반적으로 `9300`.

## REST API
- HTTP를 통해 Elasticsearch에 Document 저장, 검색, 수정, 삭제 등의 요청을 보내는 인터페이스.

## Bulk API
- 여러 Document의 저장, 수정, 삭제를 하나의 요청으로 묶어 처리하는 API.

---
# 백업과 원격 Cluster
## Snapshot
- Elasticsearch Index와 Cluster 데이터를 외부 저장소에 백업하는 기능.

## Searchable Snapshot
- Snapshot 데이터를 완전히 복구하지 않고도 검색할 수 있도록 하는 기능.

## Cross-Cluster Search (CCS)
- 여러 Elasticsearch Cluster의 데이터를 하나의 검색 요청으로 조회하는 기능.

## Cross-Cluster Replication (CCR)
- 한 Elasticsearch Cluster의 Index를 다른 Cluster로 지속적으로 복제하는 기능.

## Remote Cluster Client
- 다른 Elasticsearch Cluster와 통신할 수 있도록 하는 Node Role.

---
# 기타 Node Role
## ML Node
- Elasticsearch의 이상 탐지 등 Machine Learning 기능을 수행하는 Node.

## Transform Node
- 기존 데이터를 집계하거나 형태를 변경해 새로운 형태의 Index를 만드는 작업을 수행하는 Node.