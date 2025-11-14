
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

