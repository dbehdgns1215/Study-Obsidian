
# S3 스토리지 클래스

## 접근 빈도

### 자주 접근
- S3 Standard

### 거의 접근하지 않음
- S3 Standard-IA
- S3 One Zone-IA
- S3 Glacier Instant Retrieval
- S3 Glacier Flexible Retrieval - 최대 1시간
- S3 Glacier Deep Archive - 최대 12시간

### 접근 빈도 불규칙. 자동 조정
- S3 Intelligent-Tiering


## 즉시 조회 여부

### 즉시 조회 가능
- S3 Standard
- S3 Standard-IA
- S3 One Zone-IA
- S3 Glacier Instant Retrieval
- S3 Intelligent-Tiering

### 조회 시 시간 소요
- S3 Glacier Flexible Retrieval - 최대 1시간
- S3 Glacier Deep Archive - 최대 12시간


>Glacier
>`Glacier` 스토리지 클래스는 **법/감사/규정** 목록으로 장기 보관할 때 사용함.
>이 목적이 아닌데, 거의 접근하지 않는다 -> **S3 Standard-IA** 고르자.


# S3 버전 관리, 객체 잠금, 수명 주기 정책

기본 -> 파일 중복 업로드시 파일 덮어 씌워짐. -> 기존 파일 삭제됨.
이를 방지하려면 **버전 관리** 기능을 활성화 시켜야 함.

## S3 객체 잠금
일정 기간 동안 파일의 