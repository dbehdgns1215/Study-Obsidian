

# IP, Port

## IP
- 네트워크 상의 특정 컴퓨터를 가리키는 주소

## Port
- 한 컴퓨터 내에서 실행되고 있는 특정 프로그램의 주소


# Docker
**컨테이너**를 사용하여 각각의 프로그램을 분리된 환경에서 실행 및 관리할 수 있는 툴

왜 Docker를 쓸까?
- 여러 장점이 있지만 핵심은 바로 `이식성`이다.
	- 이식성: 특정 프로그램을 다른 곳으로 쉽게 옮겨서 설치 및 실행할 수 있는 특성

## 컨테이너(Container)란?
> Docker에서 컨테이너라는 개념은 아주 중요함. 머릿속에서 컨테이너가 어떤 개념인지 대략적으떠올릴 수 있어야만 함.

윈도우 환경을 사용해보면 하나의 컴퓨터에 여러 사용자로 나눠서 사용할 수 있게끔 구성되어 있는 것을 볼 수 있음.
각 사용자의 환경에 들어가보면 독립적으로 구성되어 있어서 필요한 프로그램을 각 사용자 환경에 맞게 따로 따로 설치해주어야 함.

컨테이너도 이와 비슷한 개념임. 하나의 컴퓨터 환경 내에서 독립적인 컴퓨터 환경을 구성해서 각 환경에 프로그램을 별도로 설치할 수 있게 만든 개념임. 하나의 컴퓨터 환경 내에서 여러 개의 미니 컴퓨터 환경을 구성할 수 있게 만든 형태. 여기서 얘기하는 **미니 컴퓨터**를 보고 Docker에서는 **컨테이너**라고 부름.

![[Pasted image 20250916231959.png]]
- 여기서 컨테이너와 컨테이너를 포함하고 있는 컴퓨터를 구분하기 위해서, 컨테이너를 포함하 있는 컴퓨터를 **호스트** **컴퓨터**라고 부름.

## 컨테이너의 독립성
위 설명에서 컨테이너는 `독립적인 컴퓨터 환경`이라고 얘기했다. 구체적으로 어떤 것들이 독립적으로 관리되는지 기억해두자.
- 디스크 (저장 공간): 각 컨테이너마다 서로 각자의 저장 공간을 가지고 있다. 일반적으로 A 컨이너 내부에서 B 컨테이너 내부에 있는 파일에 접근할 수 없다.
- 네트워크 (IP, Port): 각 컨테이너마다 고유의 네트워크를 가지고 있다. 컨테이너는 각자의 IP 주를 가지고 있다.


# 이미지 다운로드
컨테이너를 실행시키려면 이미지가 필요함.
이미지는 말하자면 닌텐도 기계에 꽂을 수 있는 게임 칩 같은 느낌.



# Docker 실행

```powershell
PS C:\WINDOWS\system32> docker image ls
REPOSITORY   TAG       IMAGE ID       CREATED       SIZE
nginx        latest    d5f28ef21aab   5 weeks ago   279MB
```
- 다운받은 이미지 목록 확인

```powershell
PS C:\WINDOWS\system32> docker run --name webserver -d -p 80:80 nginx
eeadd89da9f50821732cda98f1b1a1d3416f70489b8fc9e189ea92500faefa02
```
- 도커 실행 명령어

![[Pasted image 20250924001642.png]]
- 실행 후 `localhost:80` 접속 사진

```powershell
PS C:\WINDOWS\system32> docker ps
CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS         PORTS                                 NAMES
eeadd89da9f5   nginx     "/docker-entrypoint.…"   3 minutes ago   Up 3 minutes   0.0.0.0:80->80/tcp, [::]:80->80/tcp   webserver
```
- 실행 확인 (nginx가 실행되고 있는 컨테이너 목록)

```powershell
PS C:\WINDOWS\system32> docker stop webserver
webserver
```
- 실행되고 있는 컴퓨터(컨테이너) 종료 (`Names` 값과 매칭됨)


![[Pasted image 20250924002126.png]]


## 명령어

### 이미지 조회
- `docker image ls`

### 이미지 삭제
- `docker image rm <IMAGE ID>`
- `docker image rm -f <IMAGE ID>`
	- 특정 컨테이너 중에서도 ***중단된** 컨테이너*가 사용 중인 이미지를 강제로 지움 
- `docker image rm $(docker images -q)`
	- 컨테이너에서 사용하고 있지 않는 전체 이미지를 삭제
- `docker image rm -f $(docker images -q)`


# 컨테이너(Container) 생성 / 실행

![[Pasted image 20251012013349.png]]

## 컨테이너 생성
- `docker create nginx`

## 컨테이너 조회
- `docker ps -a`
	- 사진을 보면 알겠지만 21초 전에 생성된 컨테이너가 보임.

## 컨테이너 실행
- `docker start <CONTAINER ID>`

![[Pasted image 20251012013559.png]]
- 기존의 `d3a19...` 컨테이너가 실행되어서 `STATUS`, `PORTS` 등이 변경된 것을 알 수 있음.

## 컨테이너 자동 생성
내 컴퓨터에 이미지가 다운되어 있지 않아도 **Docker Hub**로 부터 자동으로 다운받아줌.
![[Pasted image 20251012013822.png]]
- 자동으로 mysql 이미지를 다운받아옴

## 컨테이너 생성 / 실행
- 기존의 생성과 실행을 하나로 합친 명령어
- `docker run <IMAGE NAME?>`
	- `docker run nginx`
	- `docker run mysql`

## Foreground / Background

### Foreground
- 내가 실행시킨 프로그램의 내용이 화면에서 실행되고 출력되고 있는 상태
	- 실시간으로 로그같은 것들을 확인할 수 있음.
	- 단, 다른 프로그램을 실행시키거나 다른 명령어를 추가 입력하진 못함.

### Background
- 내가 실행시킨 프로그램이 컴퓨터 내부적으로 실행되는 상태
	- 실시간으로 로그같은 것들을 확인할 수는 없음.
	-  단, 다른 명령어들을 추가적으로 입력할 수는 있음.


앞선 `docker run ...` 은 명령어는 기본적으로 `Foreground` 에서 실행되기 때문에 `Background`에서 실행하려면 추가적인 옵션이 필요함.
- `docker run -d ...`
![[Pasted image 20251012014756.png]]

## 컨테이너 이름 붙여서 생성 / 실행
- `docker run -d --name <지정할 이름> <IMAGE NAME>`
	- `docker run -d --name my-web-server nginx`
![[Pasted image 20251012015144.png]]


![[Pasted image 20251012015337.png]]
- nginx를 실행시켜서 localhost:80 으로 접근하려고 해보자.

![[Pasted image 20251012015409.png]]
- 왜 접속이 안될까?
	- 우리가 nginx 컨테이너를 띄웠다: 호스트 컴퓨터 안에 미니 컴퓨터 환경을 띄웠다.
		- 미니 컴퓨터는 분리된, 독립적인 환경임.
			- -> 호스트 컴퓨터의 네트워크와 컨테이너의 네트워크가 분리됐다는 말.
			- 따라서 우리가 외부에서 접근할 수가 없음.
				- 결국 이 호스트 컴퓨터와 컨테이너를 연결해서 접속할 수 있게끔 포트를 연결해주는 작업이 필요함.

![[Pasted image 20251012015642.png]]
- `docker run -d -p <포트 번호> <IMAGE NAME>`

![[Pasted image 20251012015748.png]]
- 기존의 포트번호랑 뭔가 다르게 설정됐다!
	- 해석해보면, 사용자가 외부에서 4000번 포트로 요청을 보내면 컨테이너의 80번 포트랑 연결하겠다는 의미.

- `localhost:4000` 으로 접근해보면,
![[Pasted image 20251012015844.png]]


![[Pasted image 20251012015337.png]]
- 이제 이 그림을 이해할 수 있을 것이다.
- 외부에 있는 사용자가 4000번 포트로 요청을 보내면, 컨테이너의 80번 포트로 타고 넘어가서 nginx에 접근할 수 있는 것.
- 따라서 호스트 컴퓨터에서 컨테이너와 외부 포트와의 `포트 맵핑`이 필요한 것.



## 컨테이너 조회 / 중지 / 삭제

### 컨테이너 조회
- `docker ps`: 실행 중인 컨테이너 조회
- `docker ps -a`: 실행 중인 컨테이너 + 중단된 컨테이너 = 모든 컨테이너 조회

### 컨테이너 중지
- `docker stop <CONTAINER ID>`: 정상적인 종료 (프로세스도 다 정리하고 깔끔하게 종료)
- `docker kill <CONTAINER ID>`: 비정상적인 종료 (긴급 탈출?) 

### 컨테이너 삭제
- `docker rm <CONTAINER ID>`: 단, 컨테이너가 실행 중일 때는 지울 수 없음.
	- `docker stop <C ID>` 이후 `docker rm <C ID>`
	- `docker rm -f`: 실행 중인 컨테이너 강제 삭제
- `docker rm $(docker ps -qa)`: 중지되어 있는 모든 컨테이너 삭제


## 컨테이너 로그 조회
- `docker logs <CONTAINER ID>`
	- `docker logs --tail 몇줄출력할래 <CONTAINER ID>`: 제일 마지막부터 10줄 출력
	- `docker logs -f <CONTAINER ID>`: 기존 로그 조회 + 실시간으로 생성되는 로그도 조회
	- `docker logs -tail 0 -f <CONTAINER ID>`: 실시간으로 생성되는 로그만 조회


## 실행 중인 컨테이너 내부에 접속하기
- `docker exec -it <CONTAINER ID> <어떤 환경? -> bash 등>`
	- `docker exec -it c5e bash`
	- `root@c5ed2bdeea57:/#`
		- 이렇게 그 앞 부분이 변경된 걸 알 수 있음.
	- ![[Pasted image 20251027221233.png]]
	- 사진을 보면 뭔가 폴더 구성이 뭔가 다르다는 걸 알 수 있음.
	- 내부 컨테이너 환경에서의 폴더 구조이기 때문.
- `cd /etc/nginx`
	- 내부 컨테이너 환경에서 nginx에 접속하기 위해서 사용
	- ![[Pasted image 20251027221426.png]]
- `exit`
	- 다시 호스트 컴퓨터 환경으로 돌아가고 싶을 때


# Docker로 Redis 실행시켜보기
- `docker pull redis`
	- 이미지 내려받기
- `docker run -d -p 6379:6379 redis`
	- 사실 실행시키면, 이미지를 자동으로 찾음. 없으면 다운 받음.

- `docker image ls`
![[Pasted image 20251028004903.png]]
- `docker ps`
![[Pasted image 20251028004919.png]]

- `docker logs <CONTAINER ID>`
![[Pasted image 20251028005144.png]]

- `docker exec -it <CONTAINER ID> bash`
	- `cd ..` -> `ls`
![[Pasted image 20251028005209.png]]

![[Pasted image 20251028005415.png]]



# Docker Volume

## 컨테이너가 가진 문제점
Docker를 활용하면 특정 프로그램을 컨테이너로 띄울 수 있다. 이 프로그램에 기능이 추가되면 새로운 이미지를 만들어서 컨테이너를 실행시켜야 한다. 이때, Docker는 기존 컨테이너에서 변경된 부분을 수정하지 않고 새로운 컨테이너를 만들어서 통째로 갈아끼우는 방식으로 교체를 한다. 이게 효율적이라고 생각했던 것이다.

이런 특징 때문에 기존 컨테이너를 새로운 컨테이너로 교체하면, 기존 컨테이너 내부에 있던 데이터도 같이 삭제된다. 만약 이 컨테이너가 MySQL을 실행시키는 컨테이너였다면, MySQL에 저장된 데이터도 같이 삭제돼버린다.

따라서 컨테이너 내부에 저장된 데이터가 삭제되면 안되는 경우에는 **볼륨(Volume)**이라는 개념을 활용해야 한다.


## Docker Volume이란?
**도커의 볼륨**이란 도커 컨테이너에서 데이터를 영속적으로 저장하기 위한 방법이다. 볼륨은 컨테이너 자체의 저장 공간을 사용하지 않고, 호스트 자체의 저장 공간을 공유해서 사용하는 형태이다.

![[Pasted image 20251028213813.png]]

## 명령어
- `$ docker run -v <호스트의 디렉토리 절대경로>:<컨테이너의 디렉토리 절대경로> <이미지명>:<태그명>`

- 만약, `<호스트의 디렉토리 절대경로>`에 디랙토리가 이미 존재할 경우, 호스트의 디렉토리가 컨테이너의 디렉토리를 덮어씌운다. 
![[Pasted image 20251028213931.png]]

- 만약, `<호스트의 디렉토리 절대경로>`에 디랙토리가 존재하지 않을 경우, 호스트의 디렉토리 절대경로에 디렉토리를 새로 만들고 디렉토리에 있는 파일들을 호스트의 디렉토리로 복사해온다. ![[Pasted image 20251028214102.png]]



# Docker로 MySQL 실행시켜보기

- Docker에 MySQL 이미지 다운받기
	- `docker run -p 3306:3306 -d mysql`
	- 다운은 받아지지만, 초기 아이디 비밀번호 세팅이 되어있지 않아서 실행이 안됨.
	- 물론 그 이전에 이미 로컬에 3306 포트를 사용하는 mysql이 있기 때문에 종료시켜야됨.

### 사용중인 포트 검색
**Windows**
```java
netstat -ano | findstr [포트 번호]

netstat -ano | findstr 8080
```

### 프로세스 종료
**Windows**
```java
taskkill /f /pid [프로세스 아이디]

taskkill /f /pid 8872
```

![[Pasted image 20251028214721.png]]

![[Pasted image 20251028214751.png]]
- 정상적으로 실행시키고 ps를 찍어보니 아무 것도 안뜬다 왜 그렇지?

![[Pasted image 20251028214819.png]]
- 30초 전에 `Exited`된 mysql이 존재한다. 왜 종료됐을까?
	- log를 찍어보자.
		- `docker logs <CONTAINER ID>`

![[Pasted image 20251028214933.png]]
- 해석해보면, 패스워드가 정의되지 않아서 생긴 문제임을 알 수 있음

## mysql 초기 루트 비밀번호 (환경 변수 관련)

![[Pasted image 20251028215036.png]]
- 해결을 위해서 mysql 초기 루트 비밀번호를 세팅해주면 문제 해결
	- `-e`: 환경 변수 선언 옵션
- `docker run -e MYSQL_ROOT_PASSWORD=1234 -d -p 3306:3306 mysql`


환경 변수가 잘 선언됐는지 확인하는 법
![[Pasted image 20251028215344.png]]


![[Pasted image 20251028215500.png]]

## 실행
![[Pasted image 20251028230423.png]]
- `docker exec -it <CONTAINER ID> bash`를 통해서 컨테이너로 접속
- 이후 컨테이너에서 mysql 명령어를 실행
	- `mysql -u root -p` 이후 `password 입력`

![[Pasted image 20251028230539.png]]
- 이런 명령어들도 가능.


여기서 만약 mysql 컨테이너를 삭제하고 다시 실행한다면?
- mydb라는 데이터베이스가 사라지게 됨.
- 따라서 볼륨이 필요함.

## 볼륨 실행
`docker run -e MYSQL_ROOT_PASSWORD=1234 -d -p 3306:3306 -v D:\Docker\Downloads\docker-mysql\mysql_data:/var/lib/mysql mysql`

- 기존 `docker run`과 유사하나, 뒤에 `-v` 이하의 옵션 절이 추가됨.
	- 데이터를 저장하고 싶은 디렉토리로 먼저 이동
		- `cd D:\Docker\Downloads\docker-mysql`
	- `docker run ...`
	- `-v`: 볼륨을 사용할게
	- `D:\Docker\Downloads\docker-mysql`: 이 디렉토리에
	- `\mysql_data`: 이 디렉토리까지 새로 생성해서 (선택)
		- 위 두 줄은, mysql 데이터를 저장하고 싶은 폴더를 의미
	- `:`: 이 콜론을 기준으로 좌측은 호스트 컴퓨터에서의 위치 즉, 호스트 컴퓨터 환경 내의 주소 값이고, 우측은 mysql에서의 즉, 컨테이너 내부의 주소 값임.
	- `/var/lib/mysql`: 방금 말한대로 컨테이너 내부에서의 주소 값
	- `mysql`: 이미지명
- 결국 호스트의 주소(콜론 좌측부)를 빌려서 컨테이너 내부의 주소(콜론 우측부)와 공유해서 사용하겠다는 말.
- 이제 컨테이너를 지워도 해당 주소의 데이터는 삭제되지 않음

> 참고로 `/var/lib/mysql`는 어디서 나온건가? -> 공식 문서에 기술되어 있음.

![[Pasted image 20251028231953.png]]
- 볼륨은 쉽게 말해서 컨테이너 내부에 저장하는 게 아니라, 호스트의 저장 공간을 빌려서 거기에 저장하는 방식임.

>진짜 중요한 사실
>
>최초로 mysql을 띄울 때, 볼륨을 이용해서 mysql을 띄웠음. 그렇다면 데이터베이스 비밀번호는 볼륨에 이미 저장이 되어있음.
>따라서 다시 `mysql run -e MYSQL_ROOT_PASSWORD=newpassword ...` 한다고 해도 비밀번호가 바뀌지 않음.

- 그럼 어떻게?
	- 기존 비밀번호로 접속 후 비밀번호를 바꾸는 명령어를 날리는 방법
	- 호스트 컴퓨터에 저장된 mysql_data를 지워버리고 다시 띄우는 방법
		- rm -rf mysql_data (내가 설정한 폴더에서, `D:\Docker\Downloads\docker-mysql`)
```
Directory: D:\Docker\Downloads\docker-mysql

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
da----    2025-10-28 (화)  오후 11:12                mysql_data                                                      
PS D:\Docker\Downloads\docker-mysql>
```

- 추가로 볼륨으로 사용할 호스트의 저장 공간에 빈 디렉토리 또는 존재하지 않는 디렉토리로 설정해줘야 정상적으로 볼륨이 할당됨.
	- 그렇지 않으면 앞서 초반에 언급했던 사진처럼 호스트의 저장 공간에 있는 파일들이 컨테이너의 저장 공간에 덮어씌워지기 때문임. (우선 순위가 이럼)
	- 따라서 빈 디렉토리 또는 존재하지 않는 디렉토리로 설정하면 컨테이너가 올라가면서 기존에 있던 설정 파일과 데이터 등이 호스트 컴퓨터로 복사되게 되는 것.

- 어쨌든, 이렇게 문제 없이 볼륨을 설정했으면 그때부터는 공유되고 있기 때문에 원하는 파일을 호스트의 저장 공간에 넣어놓으면 컨테이너에서도 사용 가능함.


# Docker File

## FROM: 베이스 이미지 생성
`FROM`은 베이스 이미지를 생성하는 역할을 한다. Docker 컨테이너를 특정 초기 이미지를 기반으로 추가적인 세팅을 할 수 있다. 여기서 얘기한 `특정 초기 이미지`가 곧 베이스 이미지이다.

즉, 우리가 윈도우 컴퓨터를 새로 사서 실행시키면 기본 프로그램들이 많이 깔려있는 것을 알고있다. 베이스 이미지도 이와 똑같다. 컨테이너를 새로 띄워서 미니 컴퓨터 환경을 구축할 때 기본 프로그램이 어떤게 깔려있으면 좋겠는지 선택하는 옵션이라고 생각하면 된다.

```
FROM [이미지명]
FROM [이미지명]:[태그명]
```
- 태그명 생략시에는 최신(latest) 버전을 사용한다.

**실습**
```
FROM openjdk:17-jdk
```

**터미널**
```
docker build -t my-jdk17-server .
```
- `my-jdk17-server`: 이미지명
- `.`: 상대경로(현재 디렉토리)

**결과**
```
PS D:\Docker\docker-practice> docker image ls
REPOSITORY        TAG       IMAGE ID       CREATED       SIZE
mysql             latest    569c4128dfa6   7 days ago    1.27GB
nginx             latest    3b7732505933   3 weeks ago   236MB
redis             latest    4521b581dbdd   3 weeks ago   200MB
my-jdk17-server   latest    0fbdbb7ea6a8   3 years ago   727MB
PS D:\Docker\docker-practice>
```

```
PS D:\Docker\docker-practice> docker build -t my-jdk17-server:beta .
```
```
PS D:\Docker\docker-practice> docker image ls
REPOSITORY        TAG       IMAGE ID       CREATED       SIZE
mysql             latest    569c4128dfa6   7 days ago    1.27GB
nginx             latest    3b7732505933   3 weeks ago   236MB
redis             latest    4521b581dbdd   3 weeks ago   200MB
my-jdk17-server   latest    0fbdbb7ea6a8   3 years ago   727MB
my-jdk17-server   beta      78285487a29a   3 years ago   727MB
PS D:\Docker\docker-practice>
```
- 태그 기반으로 생성하면 TAG 열에 저렇게 들어감


```
PS D:\Docker\docker-practice> docker run -d my-jdk17-server
c27ab32efcb617291d23028c804c211cd09927cfca397197a75956052afa73ae
```
- 컨테이너 실행

```
PS D:\Docker\docker-practice> docker ps -a
CONTAINER ID   IMAGE             COMMAND    CREATED          STATUS                      PORTS     NAMES
c27ab32efcb6   my-jdk17-server   "jshell"   36 seconds ago   Exited (0) 34 seconds ago             peaceful_dewdney
```
- 실행됐다가 종료된 것을 알 수 있음. (STATUS = Exited 34 sec..)

```
CONTAINER ID   IMAGE             COMMAND    CREATED          STATUS                      PORTS     NAMES
c27ab32efcb6   my-jdk17-server   "jshell"   36 seconds ago   Exited (0) 34 seconds ago             peaceful_dewdney
PS D:\Docker\docker-practice> docker logs c27
Oct 29, 2025 3:44:01 PM java.util.prefs.FileSystemPreferences$1 run
INFO: Created user preferences directory.
|  Welcome to JShell -- Version 17.0.2
|  For an introduction type: /help intro
```
- 로그를 찍어봐도 별 문제 없음.
	- 이유로는, Docekr의 컨테이너는 내부적으로 해야할 일을 다 실행하면 자동으로 종료가 되기 때문임.

어떻게 해결할까? (꼼수)

```
FROM openjdk:17-jdk

ENTRYPOINT [ "/bin/bash", "-c", "sleep 500" ]
```

```
PS D:\Docker\docker-practice> docker build -t my-jdk17-server . 
[+] Building 1.6s (6/6) FINISHED

PS D:\Docker\docker-practice> docker run -d my-jdk17-server
b149b8713a6c9792696e65169e6b012738ae3e4f13c9296b4d86aff319855627

PS D:\Docker\docker-practice> docker ps -a
CONTAINER ID   IMAGE             COMMAND                  CREATED          STATUS                      PORTS     NAMES
b149b8713a6c   my-jdk17-server   "/bin/bash -c 'sleep…"   3 seconds ago    Up 2 seconds                          priceless_robinson
```
- 실행된다!

- 결국, 디버깅은 `docker exec -it <CONTAINER ID>`로 하게 되는데 이건 실행 중인 컨테이너만 되기 때문에 `sleep` 꼼수가 필요함.
- 종료된 컨테이너를 디버깅하려면
	- `ENTRYPOINT [ "/bin/bash", "-c", "sleep 500" ]`
	- 코드를 추가하고 Docker 내부로 진입해서 디버깅해보면 된다.

- 디버깅 방법
	- `docker logs`로 컨테이너 로그 확인
	- `docker exec -it ...`로 컨테이너 내부 직접 들어가서 확인



## COPY: 파일 복사 (이동)
`copy`는 **호스트** 컴퓨터에 있는 파일을 복사해서 **컨테이너**로 전달한다.

```
FROM ubuntu

COPY app.txt /app.txt

ENTRYPOINT [ "/bin/bash", "-c", "sleep 500" ]
```
- `COPY app.txt`: 호스트 컴퓨터에 있는 파일 (상대 경로)
- `/app.txt`: 컨테이너의 app.txt라는 파일을 해당 경로로 복사하겠다는 뜻 (절대 경로)

```
FROM ubuntu

COPY my-app /my-app/

ENTRYPOINT [ "/bin/bash", "-c", "sleep 500" ]
```
- 디렉토리 복사시에는 컨테이너 경로 끝에 `/`를 꼭 포함시켜야함.

**활용**
```
FROM ubuntu

COPY *.txt /text-files/

ENTRYPOINT [ "/bin/bash", "-c", "sleep 500" ]
```
- `*.txt`: txt 확장자 전부를
- `/text-files/`: 해당 폴더로 모두 복사

**.dockerignore**
```
readme.txt
```
- 깃 이그노어처럼 빌드하지 않을 파일 지정 가능


## ENTRYPOINT: 컨테이너가 최초로 실행될 때 수행되는 명령어
`ENTRYPOINT`는 컨테이너가 생성되고 최초로 실행될 때 수행되는 명령어를 뜻함. 쉽게 말하면 미니 컴퓨터의 전원을 키고나서 실행시키고 싶은 명령어를 적으면 됨. (시작 프로그램 느낌)

```
ENTRYPOINT [명령어...]
```

```
ENTRYPOINT ["node", "dist/main.js"]
ENTRYPOINT ["/bin/bash", "-c", "echo hello"]
```


### 스프링 부트 프로젝트를 Docker로 실행시키기
`build` 파일을 `Dockerfile Copy`를 이용해서 컨테이너로 복사하고(`.jar`)  그 컨테이너 안에서 `.jar`파일을 실행

`build` 파일 생성
- `./gradlew clean build`
	- `build` 파일 하위에 `/libs/xxx.jar` 파일 생성됨.
	- 원래라면 배포할 때 `java -jar` 이런식으로 실행시켰지만
	- 도커를 이용해 컨테이너에서 실행시키려면
```
FROM openjdk:17-jdk

COPY build/libs/*SNAPSHOT.jar app.jar

ENTRYPOINT ["java", "-jar", "/app.jar]
```
- 참고로 인텔리제이나 특정 IDE를 사용해서 `Dockerfile`을 만들어주고 해당 코드를 작성해야함.

**실행**
```
docker run -d -p 8080:8080 hello-server
```
- `-d`: 백그라운드에서
- `-p 8080:8080`: 해당 포트를 매핑해서
- `hello-server`: 라는 이미지를 실행할거야

![[Pasted image 20251102020756.png]]

## RUN: 이미지를 생성하는 과정에서 사용할 명령문 실행
`RUN`은 이미지 생성 과정에서 명령어를 실행시켜야 할 때 사용한다.

```
RUN [명령문]

RUN npm install
```

### `RUN` VS `ENTRYPOINT`
`RUN`과 `ENTRYPOINT`가 헷갈릴 때가 있다. 둘 다 같이 명령어를 실행시키는 기능을 하기 때문이다. 하지만 엄연히 둘의 사용 용도는 다름.

`RUN`
- `이미지 생성 과정`에서 필요한 명령어를 실행시킬 때 사용

`ENTRYPOINT`
- `생성된 이비지를 기반`으로 컨테이너를 생성한 직후에 명령어를 실행시킬 때 사용

### 시나리오
`git`과 `ubuntu`를 컨테이너에서 사용하고 싶어. 그런데 도커 허브에는 둘이 합쳐진 이미지가 없네?
-> 그러면 `unbuntu` 이미지를 받아와서 그 안에 `git`을 깔아야겠다!

```
FROM ubuntu

RUN apt update && apt install -y git

ENTRYPOINT ["/bin/bash", "-c", "sleep 500"]
```
- 결국 `RUN`은 환경 세팅, `ENTRYPOINT`는 내가 필요한 작업



## WORKDIR: 작업 디렉토리 지정
`WORKDIR`으로 작업 디렉토리를 전환하면 그 이후에 등장하는 모든 `RUN`, `CMD`, `ENTRYPOINT`, `COPY`, `ADD` 명령문은 해당 디렉토리를 기준으로 실행된다.

작업 디렉토리를 굳이 지정해주는 이유는 컨테이너 내부의 폴더를 깔끔하게 관리하기 위해서이다. 컨테이너도 미니 컴퓨터와 같기 때문에 `Dockerfile`을 통해 생성되는 파일들을 특정 폴더에 정리해두는 것이 추후에 관리하기 쉽다.

만약 `WORKDIR`을 쓰지 않으면 컨테이너 내부에 존재하는 기존 파일들과 뒤섞여버린다.

추가로, `docker exec -it ..` 로 진입했을 때의 최초 경로를 지정하는 역할도 한다.

```
WORKDIR [작업 디렉토리로 사용할 절대경로]

WORKDIR /usr/src/app
```


## EXPOSE: 컨테이너 내부에서 사용 중인 포트를 문서화하기
`EXPOSE`는 컨테이너 내부에서 어떤 포트에 프로그램이 실행되는지 문서화하는 역할만 한다.
`docker -p 8080:8080`와 같은 명령어의 `-p` 옵션과 같은 역할은 일체 하지 않는다. 쉽게 표현하자면 `EXPOSE` 명령어는 쓰나 안쓰나 작동하는 방식에는 영향을 미치지 않는다.

```
EXPOSE [포트 번호]

EXPOSE 3000
```
- 결국 그냥 주석과 같은 역할임 (?)
	- 있든 없든 정상적으로 작동하며, 일종의 문서화 역할만 하는 것. 


# Docker Compose

## Docker Compose란?
여러 개의 Docker 컨테이너들을 하나의서비스로 정의하고 구성해서, 하나의 묶음으로 관리할 수 있게 도와주는 도구.

- 여러 개의 컨테이너를 관리하는 데 용이함
	- 여러 개의 컨테이너로 이루어진 복잡한 애플리케이션을 한 번에 관리할 수 있게 해준다.
	- 여러 컨테이너를 하나의 환경에서 실행하고 관리하는 데 도움이 된다.

- 복잡한 명령어로 실행시키려던 걸 간소화시킬 수 있음.
	- 복잡한 명령어 대신 `docker compose up` 명령어만 실행시키면 된다.