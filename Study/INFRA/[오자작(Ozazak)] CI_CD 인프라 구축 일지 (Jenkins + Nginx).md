
**작성일:** 2026년 1월 28일

**목표:** AWS EC2 단일 서버에 Nginx(리버스 프록시)를 앞단에 두고, 백엔드와 젠킨스를 도메인 기반으로 분리하여 배포한다.

---

### 1. 아키텍처 구조 (Architecture)

보안을 위해 80번 포트 하나만 열고, 도메인 주소에 따라 내부 접속을 분기함.

- **외부 접속 (Port 80):** Nginx (Gateway)
    
- **라우팅 규칙:**
    
    1. `http://jenkins.13.124.6.228.nip.io` 👉 **젠킨스 컨테이너 (Port 8080)**
        
    2. `http://ozazak.13.124.6.228.nip.io` (또는 IP 접속) 👉 **백엔드 컨테이너 (Port 8080)**
        

---

### 2. Docker Compose 설정 (인프라 구성)

**파일:** `docker-compose-prod.yml`

- Nginx, Backend, Jenkins, DB, Redis를 하나의 네트워크(`ozazak-network`)로 묶음.
    
- 젠킨스 데이터는 `~/jenkins/jenkins_home`에 영구 저장.

```YAML
version: '3.8'

services:
  # 1. Nginx (교통 정리) - 유일하게 외부 노출 (80:80)
  nginx:
    image: nginx:latest
    container_name: ozazak-nginx
    ports:
      - "80:80"
    volumes:
      - ./nginx/conf.d:/etc/nginx/conf.d
    depends_on:
      - back
      - jenkins
    networks:
      - ozazak-network
    restart: always

  # 2. Jenkins (배포 도구) - 외부 포트 없이 내부 통신만
  jenkins:
    image: jenkins/jenkins:lts-jdk17
    container_name: jenkins
    user: root
    volumes:
      - /home/ubuntu/jenkins/jenkins_home:/var/jenkins_home
      - /var/run/docker.sock:/var/run/docker.sock
      - /usr/bin/docker:/usr/bin/docker
    networks:
      - ozazak-network
    restart: always

  # 3. Backend (스프링 부트)
  back:
    container_name: ozazak-back-prod
    # ... (생략: 빌드 및 환경변수 설정) ...
    networks:
      - ozazak-network
    restart: always

  # 4. DB & Redis (생략)
  # ...

networks:
  ozazak-network:
    driver: bridge
```

---

### 3. Nginx 설정 (라우팅 규칙)

**파일:** `nginx/conf.d/app.conf`

- `server_name`을 이용해 요청 주소를 판별하고 적절한 컨테이너로 토스함.

```Nginx
# 1. 백엔드 (기본값: IP로 접속하거나 ozazak 주소로 접속 시)
server {
    listen 80 default_server;
    server_name _; # 모든 주소 허용 (프리패스)

    location / {
        proxy_pass http://back:8080;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}

# 2. 젠킨스 (jenkins... 주소로 접속 시에만)
server {
    listen 80;
    server_name jenkins.13.124.6.228.nip.io;

    location / {
        proxy_pass http://jenkins:8080;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
```

---

### 4. 젠킨스 초기 설정 (Initial Setup)

#### 4-1. 접속 및 잠금 해제

1. 브라우저 접속: `http://jenkins.13.124.6.228.nip.io`
    
2. **Unlock Jenkins** 화면이 뜨면 초기 비밀번호 입력 필요.
    
3. 터미널에서 비밀번호 확인 명령어:
    
```Bash
sudo cat ~/jenkins/jenkins_home/secrets/initialAdminPassword
```

```Bash
docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword
```


#### 4-2. 플러그인 설치

- **[Install suggested plugins]** 클릭.
- 기본적인 Git, Pipeline 등의 도구가 자동 설치됨 (약 2~3분 소요).

#### 4-3. 관리자 계정 생성 (Create First Admin User)

- **Username:** `admin`
- **Password:** (분실하지 않도록 주의)
- **Full name:** `Ozazak Admin`
- **E-mail:** 본인 이메일

#### 4-4. URL 설정 (Instance Configuration) **(중요)**

- Jenkins URL: **`http://jenkins.13.124.6.228.nip.io/`**
- _주의: localhost로 되어 있다면 반드시 위 도메인 주소로 변경해야 추후 배포 시 에러가 안 남._

---

### ✅ 완료 상태

이제 젠킨스 대시보드(메인 화면)에 접속할 수 있으며, **"새로운 Item"** 을 생성하여 파이프라인을 구축할 준비가 완료됨.
