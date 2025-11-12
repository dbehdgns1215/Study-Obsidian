
![[asdf 1.png]]

### user
유저 테이블
- 역할
	- 1: 일반 사용자
	- 2: 관리자

### user_health
유저 건강 정보 테이블

### oauth_account
OAuth 관련 테이블

### refresh_token
JWT refresh token 테이블

### password_reset_token
Password reset token 테이블

### nutrition_summary
일간, 주간, 월간 요약 리포트 테이블
- granularity
	- 일간, 주간, 월간
- 
### quick_add_food_code
자주 추가하는 음식을 빨리 추가하기 위한 테이블

### food_nutrition
음식 영양 정보 테이블

### diet_log_items
각 끼니에 대한 정보 테이블

### diet_logs
하루치 식사에 대한 정보 테이블

### meal_history
diet_logs 백업 테이블
- 미사용시 삭제 예정

### meal
diet_log_items 백업 테이블
- 미사용시 삭제 예정

### comment
댓글 정보 테이블

### post
게시글 정보 테이블

### post_report
게시글 신고 정보 테이블

