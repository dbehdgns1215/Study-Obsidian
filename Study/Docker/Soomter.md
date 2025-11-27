
# EC2 

Node 서버 + mysql ?

```powershell
# Docker는 각 운영 체제별로 설치 지침을 제공합니다.
# 공식 문서는 https://docker.com/get-started/에서 확인하세요.

# Node.js Docker 이미지를 풀(Pull)하세요:
docker pull node:24-alpine

# Node.js 컨테이너를 생성하고 쉘 세션을 시작하세요:
docker run -it --rm --entrypoint sh node:24-alpine

# Verify the Node.js version:
node -v # Should print "v24.11.1".

npm 버전 확인:
npm -v # 11.6.2가 출력되어야 합니다.

```

```powershell
docker pull mysql:8.1
```

![[Pasted image 20251126232047.png]]


docker-compose.yml
```yml
version: '3.9'
services:
  mysql:
    image: mysql:8.1
    container_name: my-mysql
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: soomter
      MYSQL_DATABASE: soomter
    ports:
      - "3306:3306"  # EC2 외부에서 직접 접근 필요 시
    volumes:
      - mysql-data:/var/lib/mysql

  node:
    build: ./backend
    container_name: my-node
    restart: always
    working_dir: /app
    volumes:
      - ./backend:/app
    command: sh -c "npm install && node server.js"
    ports:
      - "8080:8080"
    depends_on:
      - mysql

volumes:
  mysql-data:
```




# 로컬

node.js 다운

android studio 다운
- 애뮬레이터 다운
https://github.com/DiemasMichiels/emulator/blob/main/WINDOWS.md

vscode
- React-native 다운
- Android iOS Emulator

cmd
- node

expo go
- cmd에서 package 있는 경로에서 `npx expo start`



Ctrl + Shift + P > Emulator 선택


- node 서버 띄우는 것 까지 성공
- 결국엔 자바랑 달라서 프로젝트 전체를 ec2에 올려줘야함.
- 


# 참고 자료
https://developers.kakao.com/docs/latest/ko/tutorial/login#access-browser

https://developers.kakao.com/docs/latest/ko/kakaologin/rest-api

https://developers.kakao.com/docs/latest/ko/kakaologin/rest-api#before-you-begin-process



https://velog.io/@clean01/Project-JWT%EC%99%80-oauth2%EB%A5%BC-%EC%9D%B4%EC%9A%A9%ED%95%B4%EC%84%9C-%EC%B9%B4%EC%B9%B4%EC%98%A4-%EB%A1%9C%EA%B7%B8%EC%9D%B8-%EA%B5%AC%ED%98%84#overview



# DB

```sql
create database soomter;

use soomter;

CREATE TABLE users (
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,    -- 내부 DB용 PK
    kakao_id BIGINT UNSIGNED NOT NULL UNIQUE,      -- 카카오 고유 ID
    email VARCHAR(255),                            -- 카카오에서 제공하면 저장
    nickname VARCHAR(50),                          -- 닉네임
    profile_image_url VARCHAR(500),               -- 프로필 이미지 URL
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
);

INSERT INTO users (kakao_id, email, nickname, profile_image_url) VALUES
(1234567890, 'alice@example.com', 'Alice', 'https://example.com/alice.png'),
(2345678901, 'bob@example.com', 'Bob', 'https://example.com/bob.png'),
(3456789012, 'charlie@example.com', 'Charlie', 'https://example.com/charlie.png');
```



# 스프링부트 추가 
```yml
version: '3.9'
services:
  mysql:
    image: mysql:8.1
    container_name: my-mysql
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: soomter
      MYSQL_DATABASE: soomter
    ports:
      - "3306:3306"
    volumes:
      - mysql-data:/var/lib/mysql

  spring:
    build:
      context: ./backend/spring
      dockerfile: Dockerfile
    container_name: my-spring
    restart: always
    ports:
      - "8080:8080"
    environment:
      SPRING_DATASOURCE_URL: jdbc:mysql://mysql:3306/soomter
      SPRING_DATASOURCE_USERNAME: soomter
      SPRING_DATASOURCE_PASSWORD: soomter
    depends_on:
      - mysql

  node:
    build:
      context: ./backend/node
      dockerfile: Dockerfile
    container_name: my-node
    restart: always
    working_dir: /app
	volumes:
	  - ./backend/node:/app
	  - node_modules:/app/node_modules
    command: sh -c "npm install && node server.js"
    ports:
      - "8081:8081"
    depends_on:
      - mysql
      - spring

volumes:
  mysql-data:
```

## Node
```dockerfile
FROM node:18-alpine

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

EXPOSE 8081

CMD ["node", "server.js"]
```


## Spring Boot
```dockerfile
# 1단계: Gradle로 빌드
FROM gradle:8.10-jdk17-alpine AS builder
WORKDIR /app

# Gradle 설정 먼저 복사 (캐시용)
COPY build.gradle.kts settings.gradle.kts gradlew ./ 
COPY gradle ./gradle

# 의존성 캐시
RUN ./gradlew dependencies --no-daemon || true

# 실제 소스 복사 후 빌드
COPY . .
RUN ./gradlew clean bootJar --no-daemon

# 2단계: 실행용 이미지
FROM eclipse-temurin:17-jdk-alpine
WORKDIR /app

COPY --from=builder /app/build/libs/*.jar app.jar

EXPOSE 8080
ENTRYPOINT ["java", "-jar", "app.jar"]
```

---

# 개발용

# 프로젝트 구조
```css
project-root/
├─ docker-compose.dev.yml
└─ backend/
   ├─ node/
   │   ├─ package.json
   │   ├─ server.js
   │   └─ ... (소스 전체)
   └─ spring/
       ├─ build.gradle.kts
       ├─ settings.gradle.kts
       ├─ gradlew
       ├─ gradle/
       └─ src/
           ├─ main/
           │   ├─ java/
           │   └─ resources/
           └─ test/
```


## docker-compose.dev.yml
```yml
# 개발용 Dockerfile
version: '3.9'
services:
  mysql:
    image: mysql:8.1
    container_name: dev-mysql
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: soomter
      MYSQL_DATABASE: soomter
    ports:
      - "3306:3306"
    volumes:
      - mysql-data:/var/lib/mysql
    healthcheck:
      test: ["CMD", "mysqladmin", "ping", "-h", "localhost"]
      interval: 5s
      timeout: 5s
      retries: 10

  spring:
    build:
      context: ./backend/spring
      dockerfile: Dockerfile.dev
    container_name: dev-spring
    working_dir: /app
    volumes:
      - ./backend/spring:/app
      - ~/.gradle:/home/gradle/.gradle
    ports:
      - "8080:8080"
    environment:
      SPRING_DATASOURCE_URL: jdbc:mysql://mysql:3306/soomter
      SPRING_DATASOURCE_USERNAME: root
      SPRING_DATASOURCE_PASSWORD: soomter
    depends_on:
      - mysql

  node:
    build:
      context: ./backend/node
      dockerfile: Dockerfile.dev
    container_name: dev-node
    working_dir: /app
    volumes:
      - ./backend/node:/app
      - node_modules:/app/node_modules
    ports:
      - "8081:8081"
    depends_on:
      - mysql
      - spring

volumes:
  mysql-data:
  node_modules:
```


## Spring 개발용 Dockerfile (`backend/spring/Dockerfile.dev`)
```dockerfile
# 개발용 Dockerfile
FROM gradle:8.10-jdk17-alpine

WORKDIR /app

# 소스 마운트로 들어온 프로젝트 그대로 실행
# gradle 캐시를 홈 디렉토리에 저장
VOLUME /home/gradle/.gradle

# 컨테이너 시작 시 bootRun
CMD ["./gradlew", "bootRun"]

```

## Node 개발용 Dockerfile (`backend/node/Dockerfile.dev`)
```dockerfile
FROM node:18-alpine

WORKDIR /app

# node_modules는 컨테이너 전용 볼륨
VOLUME /app/node_modules

# 개발 서버 명령
CMD ["sh", "-c", "npm install && npm run dev"]

```