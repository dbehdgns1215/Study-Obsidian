

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

![[Pasted image 20251028215036.png]]
- 해결을 위해서 mysql 초기 루트 비밀번호를 세팅해주면 문제 해결
	- `-e`: 환경 변수 선언 옵션


환경 변수가 잘 선언됐는지 확인하는 법
![[Pasted image 20251028215344.png]]


![[Pasted image 20251028215500.png]]
