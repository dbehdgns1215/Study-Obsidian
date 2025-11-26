
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
```
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

expo



Ctrl + Shift + P > Emulator 선택


- node 서버 띄우는 것 까지 성공
- 결국엔 자바랑 달라서 프로젝트 전체를 ec2에 올려줘야함.
- 


# 참고 자료
https://developers.kakao.com/docs/latest/ko/tutorial/login#access-browser

https://developers.kakao.com/docs/latest/ko/kakaologin/rest-api

https://developers.kakao.com/docs/latest/ko/kakaologin/rest-api#before-you-begin-process



https://velog.io/@clean01/Project-JWT%EC%99%80-oauth2%EB%A5%BC-%EC%9D%B4%EC%9A%A9%ED%95%B4%EC%84%9C-%EC%B9%B4%EC%B9%B4%EC%98%A4-%EB%A1%9C%EA%B7%B8%EC%9D%B8-%EA%B5%AC%ED%98%84#overview
