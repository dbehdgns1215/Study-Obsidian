
![[Pasted image 20251121201742.png]]
- 서버 배포용으로는 `우분투` 선택
	- 윈도우나 맥에 비해서 다른 기능이 없어서 가움.
- 인스턴스 유형은 `t3.micro` 현재 프리티어 중에서가장 낮은 사양
- 키페어 -> EC2 컴퓨터에 접근할 때 사용하는 비밀번호

![[Pasted image 20251121202142.png]]
![[Pasted image 20251121202231.png]]
- 네트워크 설정 부분
	- `보안 그룹`이란 AWS 클라우드에서의 네트워크 보안을 의미함.
	- EC2 인스턴스를 `집`으로 생각한다면, 보안 그룹은 `집 바깥쪽`에 쳐져있는 울타리와 대문이고 생각하면 된다.
	- 집 바깥쪽에서 집으로 접근해도 되는지 안되는지 검사해주는 것과 동일.
![[Pasted image 20251121202447.png]]
- Inbound traffic
	- 외부에서 EC2로 보내는 트래픽
- Outbound traffic
	- EC2 인스턴스에서 외부로 나가는 트래픽


![[Pasted image 20251121202708.png]]
- 기본적으로 `Inbound 보안 그룹 규칙`에 `ssh`가 `22`번 포트에 할당되어 있음.


![[Pasted image 20251121202833.png]]
- 추가적으로 백엔드 서버를 80번 포트에 띄울 예정이기 때문에 보안 그룹 규칙에 추가해줌.
- 참고로 소스 유형은 꼭 `위치 무관`으로 설정해야함.



![[Pasted image 20251121202944.png]]
- 스토리지 구성 (Elastic Block Storage)
	- EC2에 부착된 일종의 하드디스크
	- 스토리지(Storage), 볼륨(Volume)라고도 불림
	- 정책 바뀜에 따라서 `프로비저닝(provisioned)한 GB‑수 × 월(GB‑month)`에 따라 과금되기에 16GB로 설정함
	- 기존 레거시 프리티어에서는 30GB까지는 무료였음..

![[Pasted image 20251121212422.png]]
![[Pasted image 20251121212620.png]]
- EC2 ON!

### EC2에 Docker, Docker Compose 설치
```
sudo apt-get update && \ sudo apt-get install -y apt-transport-https ca-certificates curl software-properties-common && \ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add - && \ sudo apt-key fingerprint 0EBFCD88 && \ sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" && \ sudo apt-get update && \ sudo apt-get install -y docker-ce && \ sudo usermod -aG docker ubuntu && \ newgrp docker && \ sudo curl -L "https://github.com/docker/compose/releases/download/2.27.1/docker-compose-$(uname -s)-$(uname -m sudo chmod +x /usr/local/bin/docker-compose && \ sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
```