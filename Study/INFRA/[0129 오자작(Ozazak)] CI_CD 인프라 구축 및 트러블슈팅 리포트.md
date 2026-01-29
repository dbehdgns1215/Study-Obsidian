
**작성일:** 2026년 1월 29일

**프로젝트:** AI 자소서 서비스 (ozazak)

CI/CD 인프라 구축 및 트러블슈팅 리포트

---

## 🏗 1. 인프라 아키텍처

이번 프로젝트는 **Docker-out-of-Docker (DooD)** 구조를 채택하여 Jenkins 컨테이너가 호스트의 Docker 엔진을 공유하여 배포를 수행합니다.

### 기술 스택

- **CI/CD:** Jenkins (LTS-JDK17)
    
- **Container:** Docker, Docker Compose
    
- **Backend:** Java 17, Spring Boot 3.2.1
    
- **AI:** Python 3.11 (FastAPI, Uvicorn)
    
- **DB/Cache:** PostgreSQL 15, Redis 7-alpine
    
- **Server:** AWS EC2 (Ubuntu) / Nginx
    

---

## 🛠 2. 주요 트러블슈팅 내역

### ❌ Issue 1: `docker-compose: not found` 에러

- **현상:** Jenkins 파이프라인 배포 단계에서 `exit code 127` 발생.
- **원인:** Jenkins 컨테이너 내부에 `docker-compose` 바이너리가 없거나 PATH 설정이 안 됨.
- **해결:** Jenkinsfile 내부에서 `curl`을 통해 `docker-compose`를 직접 다운로드하고 실행 권한을 부여한 뒤, `./docker-compose` 경로를 명시하여 실행하도록 수정.

### ❌ Issue 2: Jenkins 컨테이너 자살(Self-Termination) 문제

- **현상:** 배포 도중 `Container jenkins Recreate` 로그와 함께 Jenkins가 꺼지고 빌드가 중단됨.
- **원인:** `docker-compose-prod.yml` 안에 Jenkins 서비스가 포함되어 있어, 전체를 `up` 할 때 Jenkins가 자기 자신을 갱신하려 시도함.
- **해결:** 배포 명령어 뒤에 대상 서비스(`back`, `ai-service`, `nginx` 등)를 명시하여 Jenkins 서비스는 건드리지 않도록 격리.

### ❌ Issue 3: 메모리 부족으로 인한 서비스 종료 (OOM Killer)

- **현상:** 빌드 및 컨테이너 교체 시 `Exited (143)` 발생하며 서비스가 뻗고 502 Bad Gateway 노출.
- **원인:** 프리티어급(1GB RAM) 환경에서 Jenkins와 Spring Boot가 동시에 가동될 때 메모리 임계치 초과.
- **해결:**
	1. EC2 호스트 서버에 **2GB 스왑 메모리(Swap)** 설정.
    2. `docker-compose up` 시 `--no-build` 옵션을 사용하여 빌드와 실행 부하를 분리.

---

## 📄 3. 최종 Jenkinsfile (핵심 스크립트)



```Groovy
pipeline {
    agent any
    stages {
        stage('Git Clone') { ... }
        
        stage('Prepare Environment Files') {
            steps {
                script {
                    dir('back') { withCredentials([file(credentialsId: 'back-env', variable: 'ENV')]) { sh 'cp $ENV .env' } }
                    dir('ai') { withCredentials([file(credentialsId: 'ai-env', variable: 'ENV')]) { sh 'cp $ENV .env' } }
                }
            }
        }
        
        stage('Deploy Services') {
            steps {
                dir('back') {
                    sh 'docker build -t ozazak-backend:latest .'
                    sh 'docker build -t ozazak-ai-service:latest ../ai'
                    script {
                        sh '''
                            if [ ! -f "./docker-compose" ]; then
                                curl -SL https://github.com/docker/compose/releases/download/v2.24.1/docker-compose-linux-x86_64 -o ./docker-compose
                                chmod +x ./docker-compose
                            fi
                        '''
                        sh './docker-compose -f docker-compose-prod.yml up -d --no-build back ai-service nginx postgres redis'
                    }
                }
            }
        }
    }
}
```

---

## 💡 4. 향후 개선 사항

- **구조적 분리:** `mgmt`용(Jenkins)과 `prod`용(App) Docker Compose 파일을 완전히 분리하여 운영 안정성 확보.
- **이미지 경량화:** 빌드 이미지와 실행 이미지를 분리하는 Multi-stage Build 최적화 진행.
- **모니터링:** 502 에러 방지를 위한 헬스 체크(Health Check) 및 자동 복구 로직 강화.