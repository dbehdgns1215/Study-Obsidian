
# 🚀 게임 RAG & 지능형 에이전트 개발 로드맵 (Lucas Project)

## Phase 0: 개발 환경 및 인프라 셋업
기초 공사 단계입니다. AI 생태계가 가장 잘 구축된 Python 백엔드 환경을 권장합니다.

### 📝 해야 할 일 (Action Items)
- [ ] **데이터베이스 셋업:** PostgreSQL 설치 및 `pgvector` 익스텐션 활성화 (`CREATE EXTENSION vector;`).
- [ ] **백엔드 프레임워크 선정:** Python FastAPI 셋업 (비동기 처리와 API 문서 자동화에 유리).
- [ ] **필수 라이브러리 설치:** `langchain`, `langgraph`, `langchain-postgres`, `openai`, `psycopg2` 등.

### 📚 공부해야 할 키워드
- Python FastAPI 기본 구조 (Routing, Pydantic 모델)
- PostgreSQL `pgvector` 개념 (벡터 데이터 타입 선언 방법)
- ORM (SQLAlchemy) 또는 Raw SQL을 이용한 DB 비동기 연결 (Asyncpg)

---

## Phase 1: 정적 데이터 RAG 파이프라인 (지식의 주입)
게임 설정과 힌트(`lucas_knowledge`)를 AI가 검색할 수 있도록 벡터로 변환하여 적재하는 과정입니다.

### 📝 해야 할 일 (Action Items)
- [ ] **데이터 포맷팅:** 기획서에 있는 힌트들을 Q&A 방식("질문: ~ 답변: ~")과 자연어 스토리 방식으로 정리.
- [ ] **임베딩 스크립트 작성:** OpenAI `text-embedding-3-small` API를 호출하여 텍스트를 1536차원 벡터로 변환하는 Python 스크립트 개발.
- [ ] **DB 적재:** 변환된 벡터와 텍스트 원문, 그리고 메타데이터(chapter, topic)를 `lucas_knowledge` 테이블에 `INSERT`.
- [ ] **유사도 검색 테스트:** `SELECT * FROM lucas_knowledge ORDER BY embedding <-> '[유저 질문 벡터]' LIMIT 3;` 쿼리로 검색이 잘 되는지 터미널에서 테스트.

### 📚 공부해야 할 키워드
- LangChain `Vectorstores` (Postgres / pgvector 연동법)
- 코사인 유사도(Cosine Similarity)와 L2 거리(L2 Distance)의 차이
- RAG Chunking 전략 (데이터를 어떤 크기로 자를 것인가)

---

## Phase 2: 동적 컨텍스트 수집기 개발 (상황 인지)
유저가 질문했을 때, 현재 유저의 상태(`progress`)와 최근 행동(`logs`)을 DB에서 긁어와 AI에게 먹여줄 '상황 보고서'를 만드는 과정입니다.

### 📝 해야 할 일 (Action Items)
- [ ] **상태 스냅샷 추출 쿼리:** `user_story_progress`에서 해당 유저의 `latest_snapshot_json`(인벤토리, 플래그, 권한 등)을 가져오는 함수 개발.
- [ ] **최근 로그 추출 쿼리:** `story_action_logs`에서 특정 유저의 최근 액션 10개를 시간순으로 가져오는 함수 개발.
- [ ] **프롬프트 템플릿 설계:** 가져온 JSON 데이터들을 LLM이 이해하기 쉬운 텍스트로 예쁘게 포맷팅.
  *(예: "현재 유저는 Guest 권한이며, 인벤토리에 파편 1개를 가지고 있습니다. 최근 시도한 명령어는 다음과 같습니다...")*

### 📚 공부해야 할 키워드
- LangChain `PromptTemplate` 사용법
- JSON 데이터를 자연어로 직렬화(Serialization) 하는 프롬프트 엔지니어링 기술

---

## Phase 3: LangGraph 기반 AI 에이전트 구축 (뇌 조립)
단순한 1차원 검색을 넘어, AI가 스스로 판단하고 행동하는 순환 로직을 만듭니다.

### 📝 해야 할 일 (Action Items)
- [ ] **State(상태) 정의:** LangGraph에서 노드(작업 단계) 간에 주고받을 데이터 구조 정의 (`user_query`, `context`, `search_results`, `final_answer`).
- [ ] **노드(Node) 개발:** 1. `FetchContextNode`: Phase 2에서 만든 유저 상태 수집.
  2. `RetrieveKnowledgeNode`: Phase 1에서 만든 벡터 DB 검색.
  3. `GenerateAnswerNode`: 수집된 정보와 지식을 바탕으로 루카스의 페르소나에 맞춰 답변 생성.
- [ ] **엣지(Edge) 및 분기(Condition) 연결:** 정보가 부족하면 다시 검색하고, 충분하면 답변 노드로 넘어가도록 그래프 흐름 설계.

### 📚 공부해야 할 키워드
- **LangGraph** 핵심 개념 (StateGraph, Nodes, Edges, Conditional Edges)
- System Prompt 페르소나 부여 (루카스의 성격, 말투, 금지어 설정)
- LLM 할루시네이션 제어 (검색된 내용 외에는 대답하지 않도록 강제하기)

---

## Phase 4: API 서빙 및 프론트엔드 연동 (통신)
완성된 AI를 게임 클라이언트에서 호출할 수 있도록 엔드포인트를 엽니다.

### 📝 해야 할 일 (Action Items)
- [ ] **API 엔드포인트 개발:** `/api/chat` 과 같은 POST API 생성. (Body: `user_id`, `message`)
- [ ] **SSE(Server-Sent Events) 적용:** AI의 답변이 한 글자씩 타자 치듯(Streaming) 클라이언트로 전송되도록 구현. (게임 내 터미널 연출에 필수)
- [ ] **대화 기록 저장:** AI가 한 답변도 `story_action_logs` 혹은 별도의 `chat_history` 테이블에 저장하여 다음 대화의 문맥으로 활용.

### 📚 공부해야 할 키워드
- FastAPI `StreamingResponse` 사용법
- 클라이언트(프론트엔드)에서 SSE(EventSource) 또는 Fetch API 스트리밍 읽기 처리

---

## Phase 5: 모니터링 및 RAG 고도화 (LLMOps)
출시 전/후로 성능을 끌어올리고 비용을 최적화합니다.

### 📝 해야 할 일 (Action Items)
- [ ] **LangSmith 연동:** 환경 변수(`LANGCHAIN_API_KEY`)만 설정하여 AI의 모든 생각 과정과 지연 시간(Latency) 추적.
- [ ] **하이브리드 검색 적용 (선택사항):** 순수 벡터 검색만으로 한계가 올 경우, `pgvector`와 전통적인 텍스트 검색을 섞어서 정확도 향상.
- [ ] **시맨틱 캐싱(Semantic Cache) 적용:** "명령어 어떻게 쳐?" 와 "명령어 뭐라고 쳐야 해?" 처럼 똑같은 질문은 LLM을 안 거치고 즉시 답변하도록 Redis 등에 캐싱.

### 📚 공부해야 할 키워드
- LangSmith 대시보드 활용법
- RAG 리랭킹(Re-ranking) 개념
- GPT-4o-mini 등 경량/저비용 모델로의 프롬프트 마이그레이션 테스트