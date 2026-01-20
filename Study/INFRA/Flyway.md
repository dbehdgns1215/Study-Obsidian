# 🦅 Flyway 핵심 요약 가이드

## 1. Flyway란 무엇인가?

> **"데이터베이스를 위한 Git"**

- **역할:** DB 스키마(테이블, 컬럼 등)의 변경 이력을 관리하는 형상관리 도구.
    
- **원리:**
    
    1. 프로젝트 안에 있는 SQL 파일(`V1__...`)들을 읽는다.
        
    2. DB에 있는 `flyway_schema_history` 테이블을 확인한다.
        
    3. **아직 실행 안 된 SQL 파일만 골라서 실행**한다.
        
- **효과:** 누가 실행하든, 언제 실행하든 **항상 똑같은 DB 구조**를 보장한다.
    

## 2. 어떻게 쓰는가? (구현 3단계) - Spring Boot 기준


### Step 1. 의존성 추가 (build.gradle)

프로젝트에 Flyway 라이브러리를 심는다.

```Groovy
dependencies {
    implementation 'org.flywaydb:flyway-core'
    implementation 'org.flywaydb:flyway-database-postgresql'
}
```

### Step 2. SQL 파일 작성

약속된 폴더에 SQL 파일을 넣는다.

- **경로:** `src/main/resources/db/migration`
    
- **내용:** `CREATE TABLE`, `ALTER TABLE` 등 DDL 명령어.
    

### Step 3. 실행

서버(`Application.java`)를 실행하면 끝.

- Spring Boot가 켜질 때 Flyway가 알아서 SQL을 감지하고 DB에 반영한다.
    

## 3. 6인 팀 협업 전략 (The Strategy)

팀원이 많을 때 충돌을 막기 위한 절대 규칙이다.

### RULE 1: 버전 네이밍은 '타임스탬프'로

순차 번호(`V1`, `V2`)는 동시에 작업하면 무조건 겹친다.

- **❌ 나쁜 예:** `V3__Add_user_table.sql`
    
- **✅ 좋은 예:** `V20240120143000__Add_user_table.sql` (년월일시분초)
    
    - _Tip: 파일명 짓는 게 귀찮으면 IntelliJ 플러그인 쓰면 자동 생성해 줌._
        

### RULE 2: 한 번 커밋한 파일은 '절대 수정 금지'

이미 Git에 올라간(공유된) SQL 파일은 수정하면 안 된다.

- **상황:** `user` 테이블에 컬럼 하나 빼먹음.
    
- **❌ 금지:** 기존 파일(`V2024...create_user.sql`)을 열어서 수정. (이미 팀원들은 실행했기 때문에 에러 남)
    
- **✅ 정석:** 새로운 파일(`V2024...alter_user.sql`)을 만들어서 추가 변경 사항을 적음.
    

### 룰 3: 로컬 우선, 공용 나중

1. **Local:** 내 컴퓨터에서 SQL 만들고 서버 띄워서 잘 되나 확인.
    
2. **Git Push:** 확인되면 Git에 올림.
    
3. **Pull:** 다른 팀원들은 `git pull` 받고 서버 재시작하면 자동으로 내 변경 사항이 그들 DB에 반영됨.

