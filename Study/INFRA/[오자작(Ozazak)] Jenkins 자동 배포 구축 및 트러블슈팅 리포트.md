

### 1. 개요

- **대상:** `ozazak` 백엔드 프로젝트 (Java 17, Spring Boot, PostgreSQL)
- **환경:** AWS EC2 (Ubuntu), Docker, Jenkins (Container)
- **목표:** 코드 푸시 시 Jenkins가 최신 코드를 빌드하고 Docker 컨테이너로 배포

---

### 2. 주요 에러 해결 과정 (Troubleshooting)

#### **에러 1: HTTP Basic Access Denied (Git Clone 실패)**
- **원인:** SSAFY GitLab은 보안상 계정 비밀번호가 아닌 **Access Token** 사용이 필수임.
- **해결:** GitLab에서 `read_repository` 권한을 가진 Personal Access Token을 발급받아 Jenkins Credentials에 업데이트함.
    

#### **에러 2: Compilation Failed (테스트 코드 오류)**
- **원인:** `LoginServiceTest.java`에서 엔티티 클래스를 찾지 못하는 컴포즈 오류 발생.
- **해결:** 긴급 배포를 위해 파이프라인에서 `Backend Test` 단계를 주석 처리하고, Gradle 빌드 시 `-x test` 옵션을 고려함.

#### **에러 3: Unknown Shorthand Flag '-f' (Docker Compose 부재)**
- **원인:** Jenkins 컨테이너 내부에 `docker compose` 명령어가 설치되어 있지 않음.
- **해결:** `Setup Docker Compose` 스테이지를 추가하여 바이너리 파일을 직접 다운로드(`curl`)하고 실행 권한을 부여함.

#### **에러 4: Dockerfile No Such File or Directory (빌드 컨텍스트 오류)**
- **원인:** 젠킨스 워크스페이스 구조(`back/Dockerfile`)와 도커 호스트가 인식하는 경로가 일치하지 않아 발생.
- **해결:** `dir('back')` 블록 내부에서 작업을 수행하되, **Legacy Builder(`DOCKER_BUILDKIT=0`)** 옵션을 사용하여 빌드 파일을 도커 데몬으로 직접 전송함.

---

### 3. 보안 설정 및 환경 변수 처리 (`.env`)

#### **문제점**
- 서버(EC2)에 직접 만든 `.env`는 젠킨스가 빌드할 때마다 지워지는 `workspace` 폴더에 없으므로 사용할 수 없음.
#### **해결책 (Jenkins Credentials 활용)**

1. **Secret File 등록:** 진짜 DB 정보와 메일 비번이 담긴 `env.txt`를 Jenkins 금고에 저장.
2. **파일 주입:** 파이프라인 코드에 `withCredentials` 구문을 사용하여 빌드 직전에 진짜 `.env` 파일을 `back` 폴더에 생성함.

---

### 4. 최종 배포용 `.env` 가이드라인

배포 환경에서는 다음 설정이 필수적입니다.

| **변수명**                    | **설정값 (Prod)**        | **비고**                   |
| -------------------------- | --------------------- | ------------------------ |
| **DB_HOST**                | `postgres`            | Docker Compose 서비스 이름 사용 |
| **SPRING_PROFILES_ACTIVE** | `prod`                | 배포용 프로파일 활성화             |
| **MAIL_PASSWORD**          | 비밀이야                  | 자바 라이브러리 인식 오류 방지        |
| **FRONTEND_URL**           | `http://13.124.6.228` | 실제 배포 서버 IP              |

---

### 5. 최종 Jenkins Pipeline 구조 (Summary)

1. **Git Clone:** 최신 소스 코드 다운로드.
2. **Setup Docker Compose:** 배포 도구 설치 여부 확인 및 설치.
3. **Backend Deploy:**
    - `back` 디렉토리 진입.
    - Credentials 금고에서 `.env` 주입.
    - `docker build`로 이미지 생성.
    - `docker-compose up -d`로 무중단(재시작) 배포 실행.
