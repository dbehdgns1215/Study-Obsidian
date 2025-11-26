
# 세팅

![[Pasted image 20251121201742.png]]
![[Pasted image 20251124202209.png]]
- 서버 배포용으로는 `우분투` 선택
	- 윈도우나 맥에 비해서 다른 기능이 없어서 가벼움.
- 인스턴스 유형은 `t3.micro` 현재 프리티어 중에서 가장 낮은 사양 (무료일 땐 대안이 없음)
- 키 페어 -> EC2 컴퓨터에 접근(by SSH)할 때 사용하는 비밀번호

![[Pasted image 20251124202229.png]]
- 키 페어를 생성할 때는 예측하기 힘들게 만들어야 함.
- 물론 외부에 노출되는 것도 안됨.
- 비밀 키 만들기 = 키 페어 생성

---

## 네트워크 설정

![[Pasted image 20251121202142.png]]
![[Pasted image 20251121202231.png]]
- 네트워크 설정 부분 (첫 번째 사진 -> `편집` 클릭 -> 두 번째 사진)
	- `보안 그룹`이란 AWS 클라우드에서의 네트워크 보안을 의미함.
	- EC2 인스턴스를 `집`으로 생각한다면, 보안 그룹은 `집 바깥쪽`에 쳐져있는 울타리와 대문이고 생각하면 됨.
		- `포트`는 집의 출입구라고 생각하면 됨.
	- 집 바깥쪽에서 집으로 접근해도 되는지 안되는지 검사해주는 것과 동일.
- 이때, 인스턴스와 외부 사이에서 발생하는 트래픽은 다음과 같이 정의함
![[Pasted image 20251121202447.png]]
- Inbound traffic
	- 외부에서 EC2로 보내는 트래픽
	- 만약 보안 그룹의 Inbound 규칙이 허용되지 않으면 외부에서 EC2로 들어오는 연결은 거됨.
		- 참고로 mysql같이 EC2 내부에서만 접근이 이루어지는 것들은 절대 포트 열면 안됨.
		- 만약외부에서 mysql 서버에 접속한다면... 끔찍
- Outbound traffic
	- EC2 인스턴스에서 외부로 나가는 트래픽
	- 만약 보안 그룹의 Outbound 규칙이 허용되지 않으면 EC2가 외부로 요청을 보낼 수 없어짐.

![[Pasted image 20251121202708.png]]
- 기본적으로 `Inbound 보안 그룹 규칙`에 `ssh`가 `22`번 포트에 할당되어 있음.


![[Pasted image 20251121202833.png]]
- 추가적으로 백엔드 서버를 80번 포트에 띄울 예정이기 때문에 보안 그룹 규칙에 추가해줌.
- 참고로 소스 유형은 꼭 `위치 무관`으로 설정해야함.
	- Anywhere (0.0.0.0/0)
		- 전 세계 모든 IP 접근 허용
	- 내 IP
		- 현재 사용 중인 컴퓨터의 공인 IP에서만 접근 허용
	- Custom
		- 특정 IP에서만 접근 허용
	- Security Group
		- 해당 보안 그룹을 적용한 서버끼리만 통신 허용용



![[Pasted image 20251121202944.png]]
- 스토리지 구성 (Elastic Block Storage)
	- EC2에 부착된 일종의 하드디스크
	- 스토리지(Storage), 볼륨(Volume)라고도 불림
	- 정책 바뀜에 따라서 `프로비저닝(provisioned)한 GB‑수 × 월(GB‑month)`에 따라 과금되기에 16GB로 설정함
	- 기존 레거시 프리티어에서는 30GB까지는 무료였음..

---
# 인스턴스 실행

![[Pasted image 20251121212422.png]]
![[Pasted image 20251121212620.png]]
- EC2 ON!

### EC2에 Docker, Docker Compose 설치
```
# 1. Docker 설치
sudo apt-get update
sudo apt-get install -y apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt-get update
sudo apt-get install -y docker-ce docker-ce-cli containerd.io

# 2. 현재 사용자 docker 그룹에 추가
sudo usermod -aG docker $USER
newgrp docker

# 3. Docker Compose 설치
DOCKER_COMPOSE_VERSION=2.27.1
sudo curl -L "https://github.com/docker/compose/releases/download/${DOCKER_COMPOSE_VERSION}/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose

# 4. 설치 확인
docker -v
docker compose version

```

![[Pasted image 20251121213508.png]]

### 스프링 부트 프로젝트를 Docker로 배포하기 위해 JAR -> Image 빌드

Dockerfile
```
FROM openjdk:17-jdk

COPY build/libs/*SNAPSHOT.jar app.jar

ENTRYPOINT ["java", "-jar", "/app.jar"]
```

이후 콘솔에서
`./gralew clean build`

빌드한 이미지를 AWS에 올려야 함.

빌드한 이미지는 ECR에 올려서 사용하면 되고 또는 Docker Hub에 올리거나 다운받아서 사용하면 됨.
## ECR
Dockerfile로 만든 Docker 이미지를 push/pull 할 수 있는 AWS 전용 레지스트리

EC2에서
- `docker pull 주소`
	- 만약 ECR 사용했다면, 주소는 ECR Repository에 있음


컨테이너 실행 방법
```
docker image ls
-> 다운 받은 이미지의 id 값 찾아서

docker run -d -p 8080:8080 (스프링 부트 id)
```

---
### 맥북 오류 발생시?
로컬에서 빌드 및 로그인까지는 동일함

단, 도커를 빌드할 때 `docker build --platform linux/amd64 -t 서버명`

---
## Docker에 springboot, mysql, redis 띄우기
### docker-compose.yml
```
services:
  app:
    image: eclipse-temurin:17-jdk
    container_name: spring_app
    working_dir: /app
    volumes:
      - ./app:/app
    command: ./mvnw spring-boot:run
    ports:
      - "8080:8080"
    environment:
      SPRING_DATASOURCE_URL: jdbc:mysql://db:3306/mydb
      SPRING_DATASOURCE_USERNAME: root
      SPRING_DATASOURCE_PASSWORD: root
      SPRING_REDIS_HOST: redis
    depends_on:
      - db
      - redis

  db:
    image: mysql:8.0
    container_name: mysql_db
    environment:
      MYSQL_ROOT_PASSWORD: root
      MYSQL_DATABASE: mydb
    volumes:
      - db-data:/var/lib/mysql
    ports:
      - "3306:3306"

  redis:
    image: redis:7
    container_name: redis_cache
    ports:
      - "6379:6379"

volumes:
  db-data:
```
- 3개의 컨테이너(app, db, redis)가 있고
	- image: 어떤 이미지 쓸건지
	- container_name: 컨테이너 이름(실제로 컨테이너 내부에 컨테이너가 아니고 일종의 구분하기 위한 이름)은 뭐로 할건지
	- working_dir: 컨테이너 안에서의 **기본 작업 디렉토리** 지정 -> `command`가 실행될 때의 위가 이 디렉토리임.
	- command: 컨테이너가 시작될 때 실행할 명령어 
		- 예: `./mvnw spring-boot:run` -> Spring Boot 앱 실행
	- environment: 컨테이너 안에서 사용할 **환경 변수** 지정
	- volumes: **호스트 디렉토리 <-> 컨테이너 디렉토리** 연결 (볼륨 마운트)
	- ports: 호스트와 컨테이너 포트 연결 (없으면 당연히 외부 접속 불가능)
- `docker compose up -d --build`로 실행

![[Pasted image 20251121221844.png]]


## Dockerfile 정의
- 외부에서 이미지 받아와서 컨테이너를 띄우는 건 가능함.
- 다만 내 코드를 컨테이너 안에서 실행시킬 수 는 없음.
- `Docker Compose`는 결국 **이미지 어디서 가져오고 컨테이너를 어떻게 띄울지 관리**하기만 하기 때문.
- 반면 `Dockerfile`은 코드를 실행할 수 있는 **이미지**를 만드는 일종의 **설계도** 역할을 함.


```
```

--- 

> 안정성

만약 개발 중이라면, 호스트의 소스를 컨테이너로 바인드하고

| 빌드 도구  | 개발 실행 명령                 | JAR 빌드 명령         | JAR 실행 방식           |
| ------ | ------------------------ | ----------------- | ------------------- |
| Maven  | `./mvnw spring-boot:run` | `./mvnw package`  | `java -jar xxx.jar` |
| Gradle | `./gradlew bootRun`      | `./gradlew build` | `java -jar xxx.jar` |

방식으로 빠르게 변경을 반영하며 작업하는 것이 편리함.
- 두 명령어 모두 프로젝트를 빌드하지 않고 바로 실행하는 명령어

만약 개발 중이 아니라면, 먼저 로컬에서 `.jar`로 빌드한 뒤 해당 JAR을 Docker 이미지에 포함시키고(또는 CI에서 이미지 빌드) 그 이미지를 레지스트리(ECR 등)에 올려서 배포하는 방식이 더 안정적임.

- **개발 단계**
    - 로컬 프로젝트를 **볼륨으로 연결**해서 컨테이너에서 바로 실행.
    - 빠른 테스트와 반복 개발 가능.
- **배포 단계**
    - 프로젝트 파일을 **이미지 안으로 포함**시켜 컨테이너로 배포.
    - 다른 서버에서도 동일하게 실행 가능.


---

# 시나리오 (데모)

### **인프라**
### **Step 1) 코드 관련**

- **Spring Boot 프로젝트 소스**
    - `app/src/main/java/...`
    - `app/src/main/resources/...`
- **빌드 관련 파일**
    - `app/build.gradle`
    - `app/settings.gradle`
    - `app/gradlew` + `app/gradlew.bat` + `gradle/` 디렉토리
- **개발용 환경 파일** (옵션)
    - `.env` (DB 비밀번호, Redis 호스트 등 환경변수)

### **팀원**
### **Step 1: 프로젝트 클론**
`git clone <repo_url> cd project-root`

### **Step 2: 환경 변수 파일 설정** (옵션)
- `.env` 파일 복사/수정
- `cp .env.example .env`

### **Step 3: Docker Compose로 개발 환경 실행**
`docker compose -f docker-compose.dev.yml up --build`
- 컨테이너 안에서 자동으로 Gradle `bootRun` 실행
- 코드 수정 → 즉시 반영 가능

	#### **개발 도중 수정 사항 발생 시**
	
	##### A. Git으로 compose 파일 관리
	- `docker-compose` 파일도 프로젝트와 함께 Git에 커밋
	- 누군가 수정 → push → 팀원 pull
	- 최신 compose 파일 가져오기
	
	##### B. 기존 컨테이너 종료 및 재실행
	- compose 파일 변경 후 기존 컨테이너 재사용하면 반영 안 됨
	- 팀원은 **기존 컨테이너 종료 후 새로 빌드/실행**
	`docker compose -f docker-compose.dev.yml down docker compose -f docker-compose.dev.yml up --build`
	
	##### C. 자동화 팁
	- `docker compose up --build` → 자동으로 변경 사항 빌드
	- 변경 사항 많으면 **`down` 후 `up --build`** 하는 것이 안전

### **Step 4: DB/Redis 확인**
- DB 포트 3306 → 로컬에서 접속 가능
- Redis 포트 6379 → 로컬에서 접속 가능

### **Step 5: 개발 완료 후 종료**
`docker compose -f docker-compose.dev.yml down`


### 요약
- IDE는 로컬에서 켬
- IntelliJ, Eclipse 등에서 평소처럼 코드 수정
- 컨테이너는 docker compose가 실행
- 내부에서 ./gradlew bootRun 명령 실행 → 앱 구동
- 볼륨이 연결되어 있으므로 로컬 코드 변경 → 컨테이너에 바로 반영
- 결국 IDE는 로컬에서, 서버 실행은 컨테이너에서

