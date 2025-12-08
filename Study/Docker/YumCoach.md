# EC2 배포 가이드 - YumCoach 프로젝트

## 📋 목차
1. [아키텍처 구조](#아키텍처-구조)
2. [포트 설정 정리](#포트-설정-정리)
3. [환경변수 설정](#환경변수-설정)
4. [EC2 배포 단계](#ec2-배포-단계)
5. [로컬 개발 환경 설정](#로컬-개발-환경-설정)
6. [트러블슈팅](#트러블슈팅)

---

## 🏗️ 아키텍처 구조

### **배포 구조**
```
┌─────────────────────────────────────────┐
│         로컬 개발 환경 (Windows)          │
├─────────────────────────────────────────┤
│  Vue.js Frontend (localhost:3000)       │
│  Spring Boot Backend (localhost:8282)   │
│         ↓ 네트워크 접속                  │
│  EC2 MySQL Server (13.125.146.63:4500)  │
└─────────────────────────────────────────┘

┌─────────────────────────────────────────┐
│         EC2 인스턴스 (Ubuntu)             │
├─────────────────────────────────────────┤
│  MySQL Container (포트 4500:3306)        │
│  - 외부 접근: 4500                       │
│  - 컨테이너 내부: 3306                   │
└─────────────────────────────────────────┘
```

---

## 🔌 포트 설정 정리

### **MySQL 포트**
| 환경 | 외부 포트 | 내부 포트 | 설명 |
|------|----------|----------|------|
| **EC2** | 4500 | 3306 | `docker compose`가 `4500:3306` 매핑 |
| **로컬 접속** | 4500 | - | `MYSQL_HOST=13.125.146.63`, `MYSQL_PORT=4500` |
| **컨테이너 내부** | - | 3306 | MySQL 기본 포트 |

### **Backend 포트**
| 환경 | 포트 | 설명 |
|------|------|------|
| **로컬 Docker** | 8282 | `BACKEND_PORT=8282` |
| **로컬 브라우저** | 8282 | `http://localhost:8282` |

### **Frontend 포트**
| 환경 | 포트 | 설명 |
|------|------|------|
| **로컬 Docker** | 3000 | `FRONTEND_PORT=3000` |
| **로컬 브라우저** | 3000 | `http://localhost:3000` |

### **포트 매핑 이해**
```bash
# compose.yaml의 ports 설정
ports:
  - "4500:3306"
  
# 의미:
# 4500 (호스트 포트) : 3306 (컨테이너 포트)
# ↑ 외부에서 접근        ↑ 컨테이너 내부

# 로컬에서 EC2 MySQL 접속:
mysql -h 13.125.146.63 -P 4500 -u yumcoach -p
#        ↑ EC2 IP       ↑ 외부 포트
```

---

## ⚙️ 환경변수 설정

### **`.env` 파일 구조**

#### **EC2용 .env (EC2에서 MySQL만 실행)**
```bash
# MySQL 설정
MYSQL_HOST_DOCKER=mysql            # Docker 네트워크 내부 호스트명
MYSQL_PORT_DOCKER=3306             # 컨테이너 내부 포트
MYSQL_PORT_LOCAL=4500              # 외부 접근 포트 (호스트 포트)

MYSQL_DATABASE=yumcoach_db
MYSQL_USER=yumcoach
MYSQL_PASSWORD=yumcoach
MYSQL_ROOT_PASSWORD=yumcoach_root

# 현재 사용할 설정
MYSQL_HOST=${MYSQL_HOST_DOCKER}
MYSQL_PORT=${MYSQL_PORT_DOCKER}
```

#### **로컬용 .env (EC2 MySQL 사용)**
```bash
# MySQL 설정
MYSQL_HOST_EC2=13.125.146.63       # EC2 퍼블릭 IP
MYSQL_PORT_EC2=4500                # EC2의 외부 포트

MYSQL_DATABASE=yumcoach_db
MYSQL_USER=yumcoach
MYSQL_PASSWORD=yumcoach

# 현재 사용할 설정
MYSQL_HOST=${MYSQL_HOST_EC2}       # EC2 IP로 접속
MYSQL_PORT=${MYSQL_PORT_EC2}       # 4500 포트

# Backend/Frontend 포트
BACKEND_PORT=8282
FRONTEND_PORT=3000

# API URL
API_BASE_URL_DOCKER=http://localhost:8282/api
VITE_API_BASE_URL=${API_BASE_URL_DOCKER}

# JWT
JWT_SECRET_BASE64=c3NhZnlzc2FmeXNzYWZ5c3NhZnlzc2FmeXNzYWZ5c3NhZnlzc2FmeXNzYWZ5
JWT_ACCESS_TOKEN_VALIDITY=3600000
JWT_REFRESH_TOKEN_VALIDITY=604800000
```

### **환경변수 전달 흐름**
```
루트 .env
    ↓
compose.yaml (environment 섹션)
    ↓
Spring Boot 컨테이너
    ↓
application.properties
    ↓
Spring Boot Application
```

예시:
```yaml
# compose.yaml
backend:
  environment:
    MYSQL_HOST: ${MYSQL_HOST}      # .env에서 읽음
    MYSQL_PORT: ${MYSQL_PORT}      # .env에서 읽음
```

```properties
# application.properties
spring.datasource.url=jdbc:mysql://${MYSQL_HOST}:${MYSQL_PORT}/${MYSQL_DATABASE}
# 최종: jdbc:mysql://13.125.146.63:4500/yumcoach_db
```

---

## 🚀 EC2 배포 단계

### **1. EC2 인스턴스 생성 및 초기 설정**
```bash
# Ubuntu 22.04 LTS 선택
# 보안 그룹 설정:
# - SSH: 22 (내 IP)
# - MySQL: 4500 (내 IP 또는 0.0.0.0/0)
```

### **2. EC2에 Docker 설치**
```bash
# EC2 접속
ssh -i "yumcoach.pem" ubuntu@13.125.146.63

# Docker 설치
sudo apt update
sudo apt install -y docker.io docker-compose-plugin

# Docker 권한 설정
sudo usermod -aG docker ubuntu
exit  # 재접속 필요
```

### **3. 프로젝트 파일 업로드**
```bash
# 로컬에서 실행
scp -i "D:/SSAFY/workspace/Gwantong/yumcoach.pem" -r YumCoach ubuntu@13.125.146.63:/home/ubuntu/
```

### **4. EC2에서 .env 확인**
```bash
# EC2에서
cd ~/YumCoach
cat .env

# 확인할 내용:
# MYSQL_HOST=${MYSQL_HOST_DOCKER}  # mysql이어야 함
# MYSQL_PORT=${MYSQL_PORT_DOCKER}  # 3306이어야 함
# MYSQL_PORT_LOCAL=4500            # 외부 접근 포트
```

### **5. EC2에서 MySQL 컨테이너 실행**
```bash
# YumCoach 폴더에서
docker compose up -d mysql

# 실행 확인
docker compose ps
# NAME       STATUS          PORTS
# mysql-db   Up 30 seconds   0.0.0.0:4500->3306/tcp

# 로그 확인
docker compose logs mysql
# "ready for connections" 메시지 확인
```

### **6. EC2 보안 그룹 설정**
```
AWS 콘솔 → EC2 → 보안 그룹 → 인바운드 규칙 편집

규칙 추가:
- 유형: 사용자 지정 TCP
- 포트 범위: 4500
- 소스: 
  - 개발용: 내 IP (자동 입력)
  - 공개용: 0.0.0.0/0 (보안 주의!)
- 설명: MySQL for YumCoach
```

---

## 💻 로컬 개발 환경 설정

### **1. 로컬 .env 수정**
```bash
# D:\SSAFY\workspace\Gwantong\YumCoach\.env

MYSQL_HOST_EC2=13.125.146.63       # EC2 퍼블릭 IP로 변경
MYSQL_PORT_EC2=4500

MYSQL_HOST=${MYSQL_HOST_EC2}
MYSQL_PORT=${MYSQL_PORT_EC2}
```

### **2. compose.yaml 수정 - depends_on 주석**
```yaml
# backend 섹션에서 depends_on 주석 처리
backend:
  build:
    context: ./backend
    dockerfile: Dockerfile
  # depends_on:
  #   mysql:
  #     condition: service_healthy
```

**이유**: 로컬에는 mysql 컨테이너가 없으므로, depends_on이 있으면 backend 시작 실패

### **3. 로컬에서 Backend/Frontend 실행**
```bash
# YumCoach 폴더에서
docker compose up -d backend frontend

# 실행 확인
docker compose ps
# NAME             STATUS          PORTS
# spring-backend   Up 2 minutes    0.0.0.0:8282->8282/tcp
# vue-frontend     Up 2 minutes    0.0.0.0:3000->3000/tcp

# Backend 로그 확인
docker compose logs backend
# "Tomcat started on port 8282" 확인
```

### **4. 접속 테스트**
- Frontend: http://localhost:3000
- Backend API: http://localhost:8282/api/user/...

---

## 🔧 트러블슈팅

### **문제 1: EC2 MySQL 접속 안 됨**
```bash
# 증상
ERROR 2003 (HY000): Can't connect to MySQL server on '13.125.146.63:4500'

# 해결
1. EC2 보안그룹 4500 포트 열렸는지 확인
2. EC2에서 MySQL 컨테이너 실행 중인지 확인:
   docker compose ps
3. EC2에서 포트 매핑 확인:
   docker compose ps | grep 4500
   # 0.0.0.0:4500->3306/tcp 확인
```

### **문제 2: Backend 컨테이너 시작 실패 (depends_on 에러)**
```bash
# 증상
Error: service "mysql" is not running

# 해결
compose.yaml에서 backend의 depends_on 주석 처리:
# depends_on:
#   mysql:
#     condition: service_healthy
```

### **문제 3: Frontend에서 API 호출 404 에러**
```bash
# 증상
http://localhost:8282/user/signin - 404 Not Found

# 원인
API URL에 /api prefix 누락

# 해결
1. frontend_v1/src/services/api.js 확인:
   const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8282/api';
   # /api가 있는지 확인

2. 또는 .env에서:
   VITE_API_BASE_URL=http://localhost:8282/api
```

### **문제 4: 환경변수가 컨테이너에 전달 안 됨**
```bash
# 확인 방법
docker exec spring-backend env | grep MYSQL

# 정상 출력
MYSQL_HOST=13.125.146.63
MYSQL_PORT=4500
MYSQL_DATABASE=yumcoach_db

# 해결
1. .env 파일 수정 후 컨테이너 재시작:
   docker compose down
   docker compose up -d backend frontend

2. compose.yaml의 environment 섹션 확인:
   environment:
     MYSQL_HOST: ${MYSQL_HOST}
     MYSQL_PORT: ${MYSQL_PORT}
```

### **문제 5: IP 변경 시 재설정**
```bash
# EC2 재시작 후 IP 변경됨

# 1. 새 IP 확인 (AWS 콘솔)
# 2. 로컬 .env 수정
MYSQL_HOST_EC2=<새로운_IP>

# 3. .env만 EC2에 재전송
scp -i "yumcoach.pem" .env ubuntu@<새로운_IP>:/home/ubuntu/YumCoach/

# 4. 로컬 컨테이너 재시작
docker compose down
docker compose up -d backend frontend
```

---

## 📝 핵심 요약

### **포트 매핑 핵심**
```
EC2: 4500 (외부) → 3306 (컨테이너 내부)
로컬 → EC2:4500으로 접속
```

### **환경변수 핵심**
```bash
# EC2용
MYSQL_HOST=mysql        # 컨테이너 네트워크 내부
MYSQL_PORT=3306         # 컨테이너 내부 포트

# 로컬용
MYSQL_HOST=13.125.146.63  # EC2 IP
MYSQL_PORT=4500           # EC2 외부 포트
```

### **Docker Compose 핵심**
```bash
# EC2에서
docker compose up -d mysql

# 로컬에서
docker compose up -d backend frontend
```

### **depends_on 핵심**
```yaml
# EC2용 compose.yaml: depends_on 유지 (mysql 컨테이너 있음)
# 로컬용 compose.yaml: depends_on 주석 (mysql 컨테이너 없음)
```

---

## 🎯 빠른 참조

### **EC2 재배포**
```bash
# 1. .env 수정 (IP 변경 시)
# 2. .env 전송
scp -i "yumcoach.pem" .env ubuntu@13.125.146.63:/home/ubuntu/YumCoach/
# 3. EC2에서 재시작
ssh -i "yumcoach.pem" ubuntu@13.125.146.63
cd ~/YumCoach
docker compose down
docker compose up -d mysql
```

### **로컬 재시작**
```bash
# 1. .env 수정
# 2. 컨테이너 재시작
docker compose down
docker compose up -d backend frontend
```

### **로그 확인**
```bash
# Backend
docker compose logs backend -f

# MySQL (EC2)
docker compose logs mysql -f

# 전체
docker compose logs -f
```
