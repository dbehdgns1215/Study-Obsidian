

# 요구사항 정의/API 명세

| 분류  | 요구사항명         | 요구사항 상세                                      | 우선순위 | End-point (HTTP)                                                                 |                |
| --- | ------------- | -------------------------------------------- | ---- | -------------------------------------------------------------------------------- | -------------- |
| 식단  | 식단 작성         | 섭취한 음식을 DB에 선택하여 식단기록을 작성                    | 5    | POST /api/meals                                                                  | 모든 삭제는 소프트 딜리트 |
| 식단  | 식단 조회         | 식단 ID를 활용하여 식단 기록 내용을 조회                     | 5    | GET /api/meals/{mealId}                                                          |                |
| 식단  | 식단 디테일 조회     | 식단 ID를 활용하여 식단 기록의 상세 내용을 조회                 | 5    | GET /api/meals/{mealId}/items                                                    |                |
| 식단  | 식단 수정         | 작성한 식단기록의 내용을 수정                             | 5    | PATCH /api/meals/{mealId}                                                        |                |
| 식단  | 항목 추가/삭제      | 특정 식단에 음식 항목 추가/삭제                           | 5    | POST /api/meals/{mealId}/items, DELETE /api/meals/{mealId}/items/{itemId}        |                |
| 식단  | 식단 삭제         | 작성한 식단 기록 삭제(소프트 딜리트 권장)                     | 5    | DELETE /api/meals/{mealId}                                                       |                |
| 식단  | 오늘 식단 리스트     | 사용자의 특정 일자별 식단 목록과 합계                        | 5    | GET /api/meals?date=YYYY-MM-DD                                                   |                |
| 식단  | 최근 자주 먹은 음식   | 최근 N개/자주 먹는 음식 추천(빠른 추가)                     | 3    | GET /api/foods/frequent?limit=20                                                 |                |
| 식단  | 음식 검색         | 이름/카테고리/영양기준으로 검색(페이지네이션)                    | 5    | GET /api/foods/search?q=&page=&size=                                             |                |
| 식단  | 커스텀 음식 등록     | DB에 없는 사용자의 커스텀 음식 저장                        | 3    | POST /api/foods/custom, GET /api/foods/custom, PATCH /api/foods/custom/{id}      |                |
| 식단  | 식단 복사/템플릿     | 과거 식단 복제 또는 템플릿 저장/적용                        | 3    | POST /api/meals/{mealId}/duplicates, POST /api/meals/templates                   |                |
| 식단  | 주/월간 리포트      | 주/월 합계, 평균, 추세 그래프용 데이터 PDF로 다운받을 수 있게       | 2    | GET /api/analytics/weekly?week=YYYY-WW, GET /api/analytics/monthly?month=YYYY-MM |                |
| 회원  | 회원가입          | 이메일 중복 검사, 비밀번호 정책, 이름                       | 5    | POST /api/auth/signup, GET /api/auth/email/check?email=                          |                |
| 회원  | 로그인/로그아웃      | 액세스/리프레시 토큰 발급·갱신·파기                         | 5    | POST /api/auth/signin, POST /api/auth/token/refresh, POST /api/auth/signout      |                |
| 회원  | 내 정보 조회/수정    | 프로필 이미지, 닉네임, 비밀번호                           | 5    | GET /api/users/me, PATCH /api/users/me                                           |                |
| 회원  | 건강 프로필        | 키/몸무게/BMI/질환(당뇨/고혈압 등)                       | 5    | GET /api/users/me/health, PATCH /api/users/me/health                             |                |
| 회원  | OAuth         | 구글/카카오 등 소셜 로그인                              | 4    | POST /api/auth/oauth/{provider}                                                  |                |
| 회원  | 이메일 인증/재발송    | OAuth 아닐 경우. 회원가입/비밀번호 찾기용 메일 인증             | 5    | POST /api/auth/verify/email  <br>POST /api/auth/password/forgot                  |                |
| 회원  | 건강 프로필        | 키/몸무게/BMI/질환 등 정보 등록                         | 5    | GET/PATCH /api/users/me/health                                                   |                |
| 회원  | 알림 설정         | 푸시/이메일 알림(식사 리마인드, 리포트)                      | 3    | GET/PATCH /api/users/me/notifications                                            |                |
| 회원  | 세션/보안         | 최근 로그인 기기, 세션 종료                             | 1    | GET /api/users/me/sessions, DELETE /api/users/me/sessions/{sessionId}            |                |
| 운영  | 공지사항 목록 조회    | 모든 공지사항을 검색/페이지네이션으로 조회                      | 4    | GET /api/admin/notices                                                           |                |
| 운영  | 공지사항 등록       | 새 공지사항 생성                                    | 4    | POST /api/admin/notices                                                          |                |
| 운영  | 공지사항 상세 조회    | 특정 공지사항 단건 조회                                | 4    | GET /api/admin/notices/{id}                                                      |                |
| 운영  | 공지사항 수정       | 제목/내용/공개여부 등 수정                              | 4    | PATCH /api/admin/notices/{id}                                                    |                |
| 운영  | 공지사항 삭제       | 공지사항 삭제 (소프트 삭제 권장)                          | 4    | DELETE /api/admin/notices/{id}                                                   |                |
| 운영  | 유저 목록 조회      | 전체 사용자 목록 및 검색(이메일, 상태 등)                    | 4    | GET /api/admin/users                                                             |                |
| 운영  | 유저 상세 조회      | 특정 사용자의 상세 정보                                | 4    | GET /api/admin/users/{userId}                                                    |                |
| 운영  | 유저 상태/권한 수정   | 계정 비활성화, 관리자 권한 변경 등                         | 3    | PATCH /api/admin/users/{userId}                                                  |                |
| 운영  | 유저 삭제         | 사용자 계정 삭제(또는 비활성화 처리)                        | 3    | DELETE /api/admin/users/{userId}                                                 |                |
| 운영  | 신고 목록 조회      | 신고된 게시글/댓글 조회                                | 3    | GET /api/admin/reports                                                           |                |
| 운영  | 신고 처리         | 신고 승인/거절/조치 상태 변경                            | 3    | PATCH /api/admin/reports/{reportId}                                              |                |
| 운영  | 게시글 삭제        | 특정 게시글 삭제(신고된 글 포함)                          | 3    | DELETE /api/admin/posts/{postId}                                                 |                |
| 운영  | 댓글 삭제         | 특정 댓글 삭제                                     | 3    | DELETE /api/admin/comments/{commentId}                                           |                |
| AI  | 대체 음식 추천      | 과다/부족 영양소 기준으로 대체안 추천                        | 3    | POST /api/ai/substitute                                                          |                |
| AI  | 맞춤 코치(챗봇)     | 식단 피드백/목표 코칭/Q&A                             | 4    | POST /api/ai/coach:chat                                                          |                |
| AI  | 이상 탐지         | 갑작스런 과식/영양 불균형 패턴 감지                         | 3    | GET /api/ai/anomalies?range=...                                                  |                |
| AI  | 식단 이미지로 자동 입력 | 사용자가 이미지를 업로드 하면 AI로 해당 식단의 음식 목록 및 중량(g) 측정 | 3    | POST /api/ai/meal-images                                                         |                |

---
# Gant 차트

## 전체 일정
![[Pasted image 20251114140359.png]]

### 식단 관련
![[Pasted image 20251114140422.png]]

### 회원 관련
![[Pasted image 20251114140446.png]]

### 운영 관련
![[Pasted image 20251114140601.png]]

### AI 관련련
![[Pasted image 20251114140647.png]]

---

# WBS
### 전체 일정

| WBS 코드 | 작업명             | 설명                     | 담당       | 산출물                             | 완료 기준                        | 예상 기간 (일) |
| ------ | --------------- | ---------------------- | -------- | ------------------------------- | ---------------------------- | --------- |
| 1-1    | 요구사항 정의         | 프로젝트 요구사항 및 주요 기능 정의   | KIM / YU | 요구사항 정의서(PRD), 기능 목록표           | 요구사항 명세 문서 작성 및 팀 내부 검토 완료   | 2         |
| 1-2    | API 명세서 초안      | 주요 API 정의              | KIM / YU | API 명세서(v1), 엔드포인트 리스트          | 핵심 API 구조 정의 및 리뷰 승인         | 4         |
| 1-3    | 아키텍처 설계         | 백엔드/프론트/AI/DB 전체 구조 설계 | KIM / YU | 시스템 아키텍처 다이어그램, 모듈 구조도          | 전체 시스템 구조 문서화, 기술 스택 확정      | 4         |
| 1-4    | ERD / DB 설계     | 전체 데이터 스키마 설계          | KIM / YU | ERD, 테이블 정의서                    | 모든 테이블/관계 정의 완료 및 팀 검토 통과    | 4         |
| 1-5    | UI/UX 설계        | 와이어프레임, 사용자 흐름 정의      | KIM / YU | 와이어프레임, 사용자 플로우 차트              | 핵심 화면 구성 완료, 사용자 흐름 명확화      | 4         |
| 2-1    | 개발 환경 구축        | 개발 환경 통일 및 컨벤션 정리      | KIM / YU | 프로젝트 구조, 코드 컨벤션 정리              | 환경 동일화 완료 및 모든 팀원이 실행 성공     | 4         |
| 2-2    | 도메인 설계          | 도메인 모델 정의, 엔티티 설계      | KIM / YU | 도메인 모델링 문서, 엔티티 정의서             | 주요 도메인 + 엔티티 확정, 개발 가능 상태    | 3         |
| 2-3    | 도메인 개발          | 핵심 비즈니스 로직 개발          | KIM / YU | 도메인 서비스 코드, 유닛 테스트              | 도메인 기능 정상 동작 및 테스트 통과        | 7         |
| 3-1    | AI 이미지 분석 모델 개발 | 이미지 → 음식 검출/분류 모델 구현   | KIM      | AI 모델(v1), Inference 코드, 평가 리포트 | 기본 이미지 분석 정확도 확보(내부 기준 충족)   | 15        |
| 3-2    | AI 챗봇 모델 개발     | 식단 코칭/조언 모델 구현         | YU       | 챗봇 모델(v1), 프롬프트 세트, 응답 시나리오     | 챗봇이 주요 질문/답변 1차 수행 가능        | 10        |
| 4-1    | UI 개발           | FE 기본 화면 개발            | KIM      | 핵심 화면 UI, 라우팅 구성                | UI 주요 기능 흐름 완료, API 연동 가능 상태 | 15        |
| 4-2    | API 상세 설계       | 백엔드 상세 기능/에러/유효성 설계    | KIM / YU | API 스펙(v2), 에러 코드 정의서           | 모든 API 상세 스펙 확정 및 개발 ready   | 5         |
| 4-3    | 문서화             | 개발 문서/Swagger/사용 가이드   | KIM / YU | Swagger 문서, README, 사용 가이드      | 문서 공개형태 완성 & 팀원 확인 완료        | 3         |

### 식단 관련

| WBS 코드 | 작업명        | 설명                   | 담당  | 산출물            | 완료 기준                   | 예상 기간 (일) |
| ------ | ---------- | -------------------- | --- | -------------- | ----------------------- | --------- |
| F1     | 식단 작성      | 식단 생성 API 구현         | KIM | 식단 작성 API      | POST 요청으로 식단 생성 성공      | 3         |
| F2     | 식단 조회      | 단일 식단 조회 API         | KIM | 식단 조회 API      | 식단 ID 기반 조회 기능 정상 동작    | 3         |
| F3     | 식단 상세 조회   | 식단 항목 조회 API         | KIM | 식단 상세 API      | 식단 내 음식 항목 리스트 반환       | 3         |
| F4     | 식단 수정      | 식단 레코드 수정            | KIM | 식단 수정 API      | 수정 요청 시 변경사항 DB 반영      | 3         |
| F5     | 항목 추가/삭제   | 음식 항목 CRUD           | KIM | 항목 추가/삭제 API   | 항목 추가/삭제 정상 동작 및 반영     | 3         |
| F6     | 날짜별 리스트    | 특정 날짜 식단 전체 조회       | KIM | 날짜별 리스트 API    | 날짜 입력 시 모든 식단 리스트 반환    | 2         |
| F7     | 음식 검색      | 음식 목록 검색             | KIM | 검색 API         | 키워드 검색 시 페이징 포함 정상 작동   | 3         |
| F8     | 자주 먹는 음식   | 추천 기능                | KIM | 빈도 기반 추천 API   | 최근 데이터 기반 추천값 정확 반환     | 2         |
| F9     | 커스텀 음식     | 사용자 입력 데이터 저장        | KIM | 커스텀 음식 API     | 사용자 정의 음식 등록 성공         | 2         |
| F10    | 식단 복사/템플릿  | 과거 식단 복제             | KIM | 식단 복사 API      | 기존 식단 ID로 복사 생성 가능      | 2         |
| F11    | 주/월 리포트    | 영양 분석                | KIM | 리포트 데이터 API    | 주간/월간 통계 정상 반환          | 3         |

### 회원 관련

| WBS 코드 | 작업명        | 설명               | 담당  | 산출물           | 완료 기준                   | 예상 기간 (일) |
| ------ | ---------- | ---------------- | --- | ------------- | ----------------------- | --------- |
| U1     | 회원가입       | 이메일/비밀번호/기본정보 등록 | YU  | 회원가입 API      | 회원 DB 삽입 정상 동작          | 2         |
| U2     | 이메일 체크     | unique 여부 확인     | YU  | 중복확인 API      | 중복 이메일 시 오류 반환          | 1         |
| U3     | 로그인/로그아웃   | JWT 인증/로그아웃 처리   | YU  | 로그인/로그아웃 API  | 로그인 성공 및 토큰 발급          | 3         |
| U4     | 토큰 재발급     | refresh 토큰 기능    | YU  | 재발급 API       | 유효한 refresh로 access 재발급 | 2         |
| U5     | 내 정보 조회/수정 | 프로필 관리           | YU  | 내 정보 API      | 조회/수정 모두 정상 수행          | 3         |
| U6     | 건강 프로필     | 질환/BMI 정보 관리     | YU  | 건강 프로필 API    | 건강 정보 CRUD 정상 작동        | 3         |
| U7     | OAuth      | 소셜 로그인 연동        | YU  | OAuth 로그인 API | 구글/카카오 성공 로그인           | 4         |
| U8     | 이메일 인증     | 인증 메일/비밀번호 찾기    | YU  | 인증 메일 API     | 메일 발송 및 인증 성공 처리        | 3         |
| U9     | 세션 관리      | 기기/세션 종료         | YU  | 세션 관리 API     | 현재 로그인 기기 목록/종료 정상 동작   | 2         |


### 운영 관련

| WBS 코드 | 작업명       | 설명             | 담당  | 산출물          | 완료 기준             | 예상 기간 (일) |
| ------ | --------- | -------------- | --- | ------------ | ----------------- | --------- |
| A1     | 공지 CRUD   | 공지 생성/조회/수정/삭제 | YU  | 공지 API       | CRUD 정상 동작        | 3         |
| A2     | 유저 목록/상세  | 유저 데이터 관리      | YU  | 유저 목록/상세 API | 검색·필터·단건 조회 정상 동작 | 3         |
| A3     | 유저 수정/삭제  | 계정 제어          | YU  | 유저 수정/삭제 API | 유저 권한/상태 변경 성공    | 3         |
| A4     | 신고 처리     | 게시글/댓글 신고 관리   | YU  | 신고 처리 API    | 신고 상태값 업데이트 정상 반영 | 3         |
| A5     | 게시글/댓글 삭제 | 관리자 삭제         | YU  | 삭제 API       | 관리자 권한 삭제 정상 작동   | 2         |

### AI 관련

| WBS 코드 | 작업명    | 설명                   | 담당  | 산출물            | 완료 기준                | 예상 기간 (일) |
| ------ | ------ | -------------------- | --- | -------------- | -------------------- | --------- |
| AI1    | 이미지 분석 | 식단 이미지 → 음식/중량 분석    | KIM | 모델(v1), 분석 API | 이미지 입력 시 음식/중량 분석 성공 | 8         |
| AI2    | 챗봇     | 식단 코칭 대화 모델          | YU  | 챗봇 모델(v1)      | 기본 질문/답변 시나리오 응답 성공  | 7         |
| AI3    | 이상 탐지  | 영양 anomaly detection | KIM | 패턴 분석 로직       | 특이 패턴 감지해 응답 생성      | 7         |
|AI4|대체 음식 추천|부족 영양 → 추천|KIM|추천 알고리즘|영양 부족 시 대체 음식 추천 정상 출력|4|


---
# ERD/DB

![[asdf 2.png]]

### user
유저 테이블
- 역할
	- 1: 일반 사용자
	- 2: 관리자
- `id` INT (AUTO_INCREMENT, PK)
- `email` VARCHAR(255)
- `password` VARCHAR(255)
- `name` VARCHAR(100)
- `role` TINYINT


### user_health
유저 건강 정보 테이블
- `id` INT (AUTO_INCREMENT, PK)
- `user_id` INT
- `height` INT
- `weight` INT
- `diabetes` BOOLEAN / TINYINT(1)
- `high_blood_pressure` BOOLEAN / TINYINT(1)
- `hyperlipidemia` BOOLEAN / TINYINT(1)
- `kidney_disease` BOOLEAN / TINYINT(1)  


### oauth_account
OAuth 관련 테이블
- `id` BIGINT (PK)
- `user_id` INT
- `provider` ENUM(...)
- `provider_user_id` VARCHAR(191)
- `email` VARCHAR(255)
- `created_at` DATETIME
- `updated_at` DATETIME  


### refresh_token
JWT refresh token 테이블
- `id` BIGINT (AUTO_INCREMENT, PK)
- `user_id` INT
- `token` VARCHAR(512)
- `revoked` TINYINT(1)
- `created_at` DATETIME
- `last_used_at` DATETIME
- `expires_at` DATETIME


### password_reset_token
Password reset token 테이블
- `id` BIGINT
- `user_id` INT
- `token` VARCHAR(128)
- `used` TINYINT(1)
- `created_at` DATETIME
- `expires_at` DATETIME
- `used_at` DATETIME  


### nutrition_summary
일간, 주간, 월간 요약 리포트 테이블
- granularity
	- 일간, 주간, 월간 (집계 단위)
- period_key
	- 해당 기간의 키 문자열
		- DAILY: `'2025-11-12'`
		- WEEKLY: `'2025-W46'` (ISO-8601 주차 권장)
		- MONTHLY: `'2025-11'`
- `id` BIGINT (PK)
- `user_id` INT
- `granularity` ENUM(...)
- `period_key` VARCHAR(20)
- `total_kcal` DECIMAL(10,2)
- `total_protein` DECIMAL(10,2)
- `total_fat` DECIMAL(10,2)
- `total_carb` DECIMAL(10,2)
- `created_at` DATETIME
- `updated_at` DATETIME  


### quick_add_food_code
자주 추가하는 음식을 빨리 추가하기 위한 테이블
- `id` INT (AUTO_INCREMENT, PK)
- `user_id` INT
- `food_code` VARCHAR(50)
- `add_count` INT
- `created_at` DATETIME
- `updated_at` DATETIME  


### food_nutrition
음식 영양 정보 테이블
- `food_code` VARCHAR(50)
- `food_name` VARCHAR(200)
- `category` VARCHAR(100)
- `weight` VARCHAR(50)
- `energy_kcal` DECIMAL(10,2)
- `protein_g` DECIMAL(10,2)
- `fat_g` DECIMAL(10,2)
- `carbohydrate_g` DECIMAL(10,2)
- `sugar_g` DECIMAL(10,2)
- `sodium_mg` DECIMAL(10,2)
- `cholesterol_mg` DECIMAL(10,2)
- `saturated_fat_g` DECIMAL(10,2)
- `trans_fat_g` DECIMAL(10,2)
- `caffeine_mg` DECIMAL(10,2)


### diet_log_items
각 끼니에 대한 정보 테이블
- meal_type
	- 아침, 점심, 저녁
- `diet_log_item_id` INT (AUTO_INCREMENT, PK)
- `diet_log_id` INT
- `food_code` VARCHAR(50)
- `serving_size` DECIMAL(5,2)
- `created_at` DATETIME
- `updated_at` DATETIME  


### diet_logs
하루치 식사에 대한 정보 테이블
- `diet_log_id` INT (AUTO_INCREMENT, PK)
- `user_id` INT
- `log_date` DATETIME
- `total_calorie` DECIMAL(10,2)
- `memo` VARCHAR(500)
- `image_url` VARCHAR(500)
- `created_at` DATETIME
- `updated_at` DATETIME
- `is_deleted` TINYINT(1)
- `deleted_at` DATETIME
- `meal_type` VARCHAR(10) 


### comment
댓글 정보 테이블
- `id` INT (AUTO_INCREMENT, PK)
- `post_id` INT
- `user_id` INT
- `content` TEXT
- `created_at` DATETIME
- `is_deleted` TINYINT(1)
- `deleted_at` DATETIME


### post
게시글 정보 테이블
- `id` INT (AUTO_INCREMENT, PK)
- `title` VARCHAR(255)
- `content` TEXT
- `is_notice` TINYINT(1) ← (사진에 보이는 컬럼)
- `is_deleted` TINYINT(1) ← (사진에 보이는 컬럼)
- `user_id` INT
- `created_at` DATETIME
- `updated_at` DATETIME
- `deleted_at` DATETIME
- `deleted_by` TINYINT


### post_report
게시글 신고 정보 테이블
- `id` INT (AUTO_INCREMENT, PK)
- `post_id` INT
- `user_id` INT
- `processed` TINYINT(1)
- `created_at` DATETIME
- `processed_at` DATETIME  



---

# 유스케이스 다이어그램

![[Pasted image 20251114144613.png]]



---


# 📄 진행 중 리포트 저장소 아키텍처 설계 결정 문서

**(Progress Report Storage Architecture Decision)**

**프로젝트명**: YumCoach  
**문서 목적**:

- 진행 중 리포트 저장소(MySQL vs Redis) 최종 의사결정
    
- 기술적·운영적 근거 명시
    

---

## 1. 배경 (Context)

YumCoach 서비스는 사용자의 식사 기록을 기반으로 다음 네 가지 리포트를 제공한다.

### 리포트 유형

|구분|상태|설명|
|---|---|---|
|일일 리포트|진행 중|당일 식사 기준, 지속 업데이트|
|일일 리포트|확정|전일 리포트, 변경 불가|
|주간 리포트|진행 중|이번 주 누적 식사 기준|
|주간 리포트|확정|지난 주 리포트, 변경 불가|

진행 중 리포트는 식사 추가/수정/삭제 이벤트마다 빈번히 변경되며,  
확정 리포트는 배치 작업을 통해 한 번만 생성된다.

---

## 2. 문제 정의 (Problem Statement)

진행 중 리포트를 MySQL에 직접 저장할 경우 다음 문제가 발생한다.

1. **고빈도 UPDATE**
    
    - 식사 이벤트마다 DB Write 발생
        
    - 인덱스/락/IO 부하 증가
        
2. **저장 성격 불일치**
    
    - 진행 중 리포트는 언제든 재계산 가능
        
    - 그러나 영구 저장소(MySQL)에 저장됨
        
3. **확정/진행 데이터 혼재**
    
    - 쿼리 복잡도 증가
        
    - 테이블 관리 어려움
        

이에 따라, **진행 중 리포트의 저장소를 Redis로 분리할지**에 대한 의사결정이 필요했다.

---

## 3. 고려한 옵션 (Options Considered)

### Option A. MySQL 단독 사용

- 진행/확정 리포트 모두 MySQL에 저장
    
- `status = PROGRESS / CONFIRMED`로 구분
    

### Option B. Redis + MySQL 분리

- 진행 중 리포트: Redis
    
- 확정 리포트: MySQL
    

---

## 4. 핵심 설계 관점 (Key Design Considerations)

### 4.1 데이터 성격 분리

|항목|진행 중 리포트|확정 리포트|
|---|---|---|
|변경 빈도|매우 높음|없음|
|재계산 가능|가능|불필요|
|영구 보관 필요|없음|필수|
|AI 분석 깊이|얕음|깊음|
|장애 시 영향|낮음|높음|

---

### 4.2 정량 계산 vs AI 분석

본 프로젝트에서 리포트는 두 종류의 데이터를 포함한다.

#### 1) 정량 계산 데이터

- 칼로리, 영양소, 점수 등
    
- 결정적(deterministic)
    
- 계산 비용 낮음
    
- Redis 캐시에 적합
    

#### 2) AI 분석 데이터

- 식단 요약, 트렌드, 인사이트
    
- 비용 높음
    
- 비결정적
    
- **진행 중 단계에서는 최소화해야 함**
    

---

## 5. 최종 결정 (Decision)

### ✅ **Option B 채택: Redis + MySQL 분리 구조**

**단, 중요한 전제 조건이 있음**

> ❗ Redis는 AI 비용 절감을 위한 수단이 아니다.  
> ❗ Redis는 “고빈도 상태 관리”를 위한 메모리 캐시다.

---

## 6. 최종 아키텍처 설계 (Final Architecture)

### 6.1 저장소 역할 분담

```
┌─────────────────────────┐
│        Redis             │
│  (In-Memory Cache)       │
│                           │
│  - 일일 진행 중 리포트     │
│  - 주간 진행 중 리포트     │
│  - 정량 계산 결과          │
│  - 간단 AI 요약            │
└───────────▲─────────────┘
            │
            │ Batch Confirm
            ▼
┌─────────────────────────┐
│        MySQL             │
│  (Persistent Storage)   │
│                           │
│  - 일일 확정 리포트       │
│  - 주간 확정 리포트       │
│  - 심화 AI 분석 결과     │
└─────────────────────────┘
```

---

### 6.2 Redis 데이터 구조

#### 일일 진행 중 리포트

```
Key: daily:progress:{userId}:{date}
TTL: 48h
Value:
{
  totalCalories,
  nutrientScores,
  overallScore,
  simpleAiSummary,
  lastCalculatedAt
}
```

#### 주간 진행 중 리포트

```
Key: weekly:progress:{userId}:{weekStart}
TTL: 7d
Value:
{
  weeklyScore,
  consistencyScore,
  dailyScores,
  simpleAiSummary,
  lastCalculatedAt
}
```

---

### 6.3 MySQL 데이터 구조 (확정 리포트만)

- 확정된 리포트만 저장
    
- 진행 상태 컬럼 제거
    
- 테이블 목적 명확화
    

---

## 7. AI 분석 전략 (Critical Decision)

### 진행 중 리포트

- **AI 호출 최소화**
    
- 룰 기반 / 짧은 프롬프트
    
- 캐시 대상 아님
    
- 비용 통제 목적
    

### 확정 리포트

- 배치 기반 심화 AI 분석
    
- 패턴, 인사이트, 추천 생성
    
- MySQL에 영구 저장
    

---

## 8. 장애 및 복구 전략 (Failure Handling)

### Redis 장애 시 정책

```
Redis Down →
  진행 중 리포트 조회 →
    실시간 재계산 →
      Redis 재저장 시도 (best-effort)
```

- Redis는 언제든 초기화 가능
    
- 스냅샷(RDB/AOF)에 의존하지 않음
    
- 서비스 중단 없음
    

---

## 9. 장단점 요약

### 장점

- MySQL Write 부하 대폭 감소
    
- 실시간 UX 개선
    
- 저장소 역할 명확화
    
- 확장성 확보
    
- 확정 데이터 안정성 보장
    

### 단점

- 인프라 구성 복잡도 증가
    
- Redis 장애 시 재계산 발생
    
- 초기 학습 비용
    

---

## 10. 채택 이유 요약 (Why This Works)

1. **데이터 성격에 맞는 저장소 선택**
    
2. **AI 비용 통제 가능**
    
3. **진행 중 데이터의 휘발성 수용**
    
4. **확정 데이터의 안정성 유지**
    
5. **향후 사용자 증가에 대비한 구조**
    

---

## 11. 결론 (Final Statement)

> 본 설계는  
> “모든 데이터를 안전하게 저장하는 구조”가 아니라  
> **“저장할 가치가 있는 데이터만 영구 보관하는 구조”**를 지향한다.

진행 중 리포트는 상태(state)이며,  
확정 리포트만이 기록(record)이다.

이에 따라,  
**Redis는 상태 관리**,  
**MySQL은 기록 보관**이라는 역할 분리가 본 프로젝트에 가장 적합하다고 판단한다.

---

## 12. 부록: 의사결정 키워드

- YAGNI
    
- State vs Record
    
- Deterministic vs Non-deterministic
    
- Write-heavy workload
    
- Cost-aware AI usage


---

# 진행중 리포트 저장소 설계 분석 보고서

## 1. 문서 목적

본 문서는 식단 관리 서비스에서 **진행중 리포트(PROGRESS)** 를 저장·관리하기 위한 저장소 선택에 대해 분석하고, **MySQL 단독 사용**과 **Redis + MySQL 혼합 구조**를 비교하여 최적의 아키텍처 결론을 도출하는 것을 목적으로 한다.

특히 본 문서는 단순 성능 비교가 아닌, **정량 데이터 계산과 AI 분석 결과의 성격 차이**를 기준으로 Redis 도입의 실질적 효용을 검증한다.

---

## 2. 리포트 유형 정의

본 시스템에서 리포트는 기간과 상태에 따라 총 4가지로 구분된다.

### 2.1 일일 리포트

- **일일 진행중 리포트 (PROGRESS)**  
    당일 식사 기록을 기반으로 실시간으로 변동되는 리포트
    
- **일일 확정 리포트 (CONFIRMED)**  
    하루가 종료된 후 배치 작업을 통해 확정되며 이후 변경되지 않는 리포트
    

### 2.2 주간 리포트

- **주간 진행중 리포트 (PROGRESS)**  
    해당 주의 일일 리포트 및 식사 기록에 따라 지속적으로 변경되는 리포트
    
- **주간 확정 리포트 (CONFIRMED)**  
    주간 종료 후 배치 작업으로 확정되며 이후 변경되지 않는 리포트
    

---

## 3. 진행중 리포트의 특성 분석

진행중 리포트는 다음과 같은 공통적인 특성을 가진다.

1. **변경 빈도가 매우 높음**  
    식사 추가, 수정, 삭제 시마다 즉시 업데이트됨
    
2. **원본 데이터가 아님**  
    식사 기록(Meal Record)으로부터 언제든 재생성 가능
    
3. **정량 데이터와 AI 해석 데이터가 혼재됨**
    
    - 정량 데이터: 칼로리, 영양소, 점수 등
        
    - AI 해석 데이터: 요약 문장, 분석 코멘트, 개선 제안 등
        

이 중 **정량 데이터와 AI 해석 데이터는 성격이 근본적으로 다르다**는 점이 저장소 설계의 핵심 분기점이 된다.

---

## 4. 저장소 선택지 개요

### 4.1 선택지 A: MySQL 단독 구조

- 진행중 리포트와 확정 리포트를 모두 MySQL에 저장
    
- status 컬럼(PROGRESS / CONFIRMED)으로 구분
    

### 4.2 선택지 B: Redis + MySQL 혼합 구조

- 진행중 리포트: Redis
    
- 확정 리포트: MySQL
    

---

## 5. MySQL 단독 구조 분석

### 5.1 장점

- 단일 저장소로 인한 구조 단순성
    
- 트랜잭션 및 데이터 무결성 보장
    
- 장애 및 재시작에 강함
    
- 운영 및 배포 복잡도 낮음
    

### 5.2 단점

- 진행중 리포트의 잦은 UPDATE로 인한 Write 부하
    
- PROGRESS / CONFIRMED 데이터 혼재로 인한 테이블 복잡성
    
- 대규모 트래픽 시 성능 확장 한계
    

---

## 6. Redis 도입 시 핵심 오해와 검증

### 6.1 오해: Redis에 진행중 리포트 전체를 저장하면 성능이 획기적으로 개선된다

이 접근은 **부분적으로만 참**이며, AI 분석까지 포함할 경우 실질적 이점이 크게 감소한다.

### 6.2 이유 분석

- Redis는 I/O 성능은 뛰어나지만, AI 분석은 외부 API 호출 또는 고비용 연산임
    
- 전체 처리 시간에서 병목은 DB가 아니라 AI 분석에 존재
    
- AI 분석 결과를 매번 생성하여 Redis에 저장할 경우, Redis는 단순 임시 DB 역할로 전락함
    

결론적으로 **AI 분석 결과까지 Redis에 포함시키는 설계는 MySQL 대비 구조적 이점이 거의 없다**.

---

## 7. Redis 도입이 의미 있으려면 필요한 전제

Redis 도입이 실질적 가치를 가지기 위해서는 다음 조건이 충족되어야 한다.

1. Redis에는 **재생성 가능한 데이터만 저장**할 것
    
2. AI 분석 결과는 **빈번히 재계산되지 않을 것**
    
3. Redis 장애 시에도 서비스 로직이 정상 동작할 것
    
4. `Redis` 도입 조건
	
	- DAU 10,000+
	- 식사 이벤트로 인한 UPDATE TPS 증가 
	- 리포트 조회 지연 체감 발생
	- MySQL Write 병목 확인
	  
  
이를 만족하기 위해 진행중 리포트는 내부적으로 **데이터 계층 분리**가 필요하다.

---

## 8. 권장 아키텍처: AI 분석의 역할 분리

본 시스템에서는 AI 분석을 단일 개념으로 취급하지 않고, **목적에 따라 두 가지 유형으로 명확히 분리**한다. 이 분리는 Redis 도입 여부 및 리포트 설계의 핵심 전제가 된다.

### 8.1 리포트용 AI 분석 (Report AI)

리포트에 포함되는 AI 분석은 다음 원칙을 따른다.

- 생성 시점: **리포트 확정(CONFIRMED) 시 단 1회**
    
- 목적: 정량 계산 결과를 기반으로 한 **사실 기반 요약 및 패턴 분석**
    
- 성격:
    
    - 방향성 제시 ❌
        
    - 행동 유도 ❌
        
    - 정량 데이터 해석 ⭕
        

주요 입력 데이터:

- 총 칼로리, 영양소 합계 및 비율
    
- 식사 시간 분포
    
- 일관성 점수, 주간 점수 등
    

주요 출력:

- 식단 패턴 요약
    
- 과다/부족 섭취에 대한 객관적 분석
    
- 점수 변화에 대한 설명
    

이 분석 결과는 **리포트의 일부로서 영구 저장되며**, Redis에 저장되지 않는다.

---

### 8.2 챗봇용 AI 분석 (Chat AI)

챗봇 기능에서 사용하는 AI 분석은 리포트 AI와 목적이 근본적으로 다르다.

- 생성 시점: 사용자 요청 시점 (온디맨드)
    
- 목적: 사용자에게 **방향성, 조언, 전략적 선택지 제시**
    
- 성격:
    
    - 방향성 제시 ⭕
        
    - 목표 설정 지원 ⭕
        
    - 실험적·대화형 응답 ⭕
        

특징:

- 분석 결과는 **리포트로 저장되지 않음**
    
- 일회성 응답 또는 대화 컨텍스트로만 사용
    
- 필요 시 챌린지 생성, 목표치 설정 기능과 연계
    

이 AI는 시스템의 상태를 확정하지 않으며, 사용자의 의사결정을 돕는 보조 도구로만 동작한다.

---

### 8.3 Redis에 저장할 대상 재정의 (정량 데이터 전용)

위와 같은 AI 역할 분리를 전제로 할 때, Redis의 역할은 명확해진다.

Redis에는 다음과 같은 **정량 계산 결과만 저장**한다.

- 총 칼로리
    
- 영양소 합계 및 비율
    
- 식사 횟수
    
- 시간 분포 지표
    
- 점수(Overall, Calorie, Nutrient 등)
    

특징:

- 계산 비용이 낮음
    
- 변경 빈도가 높음
    
- Redis 장애 시 재계산 가능
    

AI 분석 결과(Report AI, Chat AI)는 Redis에 저장하지 않는다.

---

## 9. Redis 장애 및 재시작에 대한 대응 전략

Redis는 메모리 기반 저장소이므로 서버 재시작 또는 장애 시 데이터 유실 가능성이 존재한다.

본 설계에서는 이를 다음과 같이 정의한다.

- Redis 데이터 유실은 **장애가 아님**
    
- Redis는 캐시 및 작업 메모리 역할
    
- 데이터 유실 시 식사 기록을 기반으로 즉시 재계산
    

Redis 영속화(RDB/AOF)는 선택 사항이며, 성능 보조 수단으로만 사용한다.

---

## 10. 최종 결론

1. 본 시스템에서 AI 분석은 **리포트용 AI와 챗봇용 AI로 명확히 분리**된다.
    
2. 리포트에 포함되는 AI 분석은 **확정(CONFIRMED) 시점에 단 1회 생성**되며, 정량 데이터를 해석하는 데에만 목적을 둔다.
    
3. 실시간 진행중 리포트에서는 AI 분석을 수행하지 않으며, 정량 계산 결과만 유지한다.
    
4. 챗봇 AI는 방향성 및 조언 제공을 목적으로 하며, 리포트 상태를 변경하거나 저장하지 않는다.
    
5. Redis는 정량 계산 결과의 캐시 및 작업 메모리로 사용되며, AI 분석 저장소로 사용하지 않는다.
    

### 최종 권고안

- 진행중 리포트:
    
    - 정량 지표 계산
        
    - Redis 저장 (선택적)
        
    - AI 분석 미포함
        
- 확정 리포트:
    
    - 정량 지표 고정
        
    - AI 분석 생성 (Report AI)
        
    - MySQL 영구 저장
        
- 챗봇 기능:
    
    - 사용자 요청 기반 AI 분석 (Chat AI)
        
    - 리포트 비연동
        
    - 목표/챌린지 생성 기능과 연계
        

본 구조는 데이터 신뢰성, AI 비용 관리, 사용자 경험, 시스템 확장성을 모두 고려한 합리적인 설계이다.