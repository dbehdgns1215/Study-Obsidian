---

---

---
# 팀원
- 유동훈
- 박정훈

# 알고리즘 설명
---
## A. 정보 기반 가중치 구간 합에 따른 지역 추천
### 1) 개요
관광지의 평점, 검색 수, 해당 관광지 계획을 세운 유저 카운팅을 통해 각 관광지 별 점수를 계산, 이 값들을 전국 > 시, 도 > 군, 구 > 관광지의 순서로 구간합 계산하여 합이 큰 순서로 유저에게 추천
이를 통해 각 관광지의 점수가 자주 변경이 되더라도 구간합을 O(logN)의 시간복잡도로 계산이 가능

### 2) 점수 계산
$score = a ⋅  평점 + b ⋅ 검색 순위 + c ⋅ 유저 방문 횟수$
$a = 2, b = -1, c = 3$ 

### 3) 데이터 모델

- `region`(id, parent_id, level(L1: 국가, L2: 시도, L3: 군구, L4: 관광지), name, lft, rgt)
- `attraction`(id, region_id, lat, lng, base_score, …)

### 4) 인덱싱 & 세그먼트 트리 구성

- **Region Linearization**: 지역 트리를 BFS로 순회하며 인덱스 할당
- **Attraction Score Array** `A[region_idx]`: 각 지역 노드에 속한 관광지 점수
- **Segment Tree** `ST`: `A`에 대한 구간합 트리

#### 질의 & 업데이트

- **질의**: 특정 지역 R의 서브트리 합 → O(log N)
- **점 업데이트**: 관광지 점수 변경 시 속한 지역의 리프/관련 구간 갱신 → O(log N)

### 5) UI/UX

1) 사용자가 “전국” 선택 → “시·도 TOP 10” 카드형 랭킹
2) “서울” 선택 → “구 TOP 10”
3) “강남구” 선택 → “동 TOP 10”
4) 랭킹 카드에는 **점수 합계, 대표 스팟, 혼잡 예측(옵션)** 표시

### 6) 복잡도 & 장점

- **Query**: O(log N)
- **Update**: O(log N)
- 대규모 데이터(전국 수만~수십만 스팟)에도 **실시간 체감 속도** 달성
- 관광지 별 점수가 자주 바뀌더라도 빠른 시간 내에 계산이 가능


---

## B. 유사 여행지 클러스터링 알고리즘
### 1) 개요

- 사용자가 **기준 POI(예: ‘한강공원’)** 선택하면,
    1. **위치 기반**: 기준점 주변을 **공간 클러스터링**하여 동선에 맞는 묶음을 만들고,
    2. **콘텐츠 기반**: 태그/카테고리/임베딩으로 **유사 컨텐츠 클러스터**를 만들어 제안.
- 결과를 **기준점과의 최단거리**(또는 이동시간)로 재정렬하여 제시.

### 2) 데이터 모델 (요약)

- `attraction`(id, lat, lng, region_id, categories[], tags[], embedding_vector, popularity, open_hours, …)
- `route_graph`(node_id, lat, lng), `edges`(u, v, weight=$이동시간$$/$$거리$)

### 3) 위치 기반 클러스터링

- **알고리즘**:
    - 도시/밀집 환경: **DBSCAN/HDBSCAN** (eps=반경, minPts=밀도 기준)
    - 광역/희소 지역: **K-Means with K-selection (Elbow/Silhouette)**
- **스케일링**: 위경도를 등적도 투영(UTM)으로 변환해 거리 의미 보존
- **클러스터 대표점**: 중심(centroid) 또는 **가장 인기 높은 POI**

### 4) 최단거리 계산 & 정렬

- 소수 후보에는 **Haversine**(간단)
- 대중교통/보행 정확도 필요 시 **A*** 또는 **Dijkstra** on `route_graph`
- 정렬 기준 예:
    $rank=α⋅normDistance+β⋅popularity+γ⋅userAffinity\text{rank} = \alpha \cdot \text{normDistance} + \beta \cdot \text{popularity} + \gamma \cdot \text{userAffinity}$
### 5) 콘텐츠 기반 유사 추천

- **벡터화**:
    - 카테고리/태그 → one-hot/TF-IDF
    - 설명문/리뷰 → **Sentence/Doc Embedding** (e.g., all-MiniLM)
    - 결합 임베딩: `z = [category_vec || tag_vec || text_embed]`
        
- **근접 탐색**:
    - 기준 POI의 임베딩 `z*`에 대해 **ANN**(FAISS/HNSW)로 top-N 후보
    - 위치 가중: `score = sim(z*, z_i) - λ·distance(baseline, i)`

### 6) 워크플로우

1. 사용자가 기준 POI 선택(예: 한강)
2. **위치 기반** 클러스터 생성 -> 각 클러스터를 대표 카드로 요약
3. 각 클러스터 내부를 **기준점과의 최단거리** 순으로 정렬
4. 병렬로 **콘텐츠 기반** 유사 후보 top-N 생성
5. 두 리스트를 **탭/토글**로 제공 (“근처 묶음 / 비슷한 곳”)
6. “하루 일정 담기” 누르면 **TSP 근사(2-Opt/Greedy)로 방문 순서 자동 정렬

### 7) 복잡도 & 운영

- DBSCAN: 평균 O(N log N) (공간 인덱스 R-tree/KD-tree 활용)
- ANN: 서브선형 쿼리 (HNSW/FAISS)
- 거리 계산 캐시: **(baseline, gridCell) → avg ETA** 캐싱으로 체감 속도 향상
