

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

