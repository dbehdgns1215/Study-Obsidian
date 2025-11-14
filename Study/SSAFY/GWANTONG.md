

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


# Gant 차트



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

## 전체 요약
![[Pasted image 20251114133918.png]]

### 회원 시스템
![[스크린샷 2025-11-14 133031 1.png]]

### 식단 시스템
![[스크린샷 2025-11-14 133323.png]]

### AI 시스템
![[스크린샷 2025-11-14 133504.png]]

### 커뮤니티 시스템
![[스크린샷 2025-11-14 133721.png]]

### 운영 시스템
![[스크린샷 2025-11-14 133420.png]]

---

