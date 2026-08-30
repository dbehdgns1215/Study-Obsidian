
# S3 스토리지 클래스

## 접근 빈도

### 자주 접근
- S3 Standard

### 거의 접근하지 않음
- S3 Standard-IA
- S3 One Zone-IA
- S3 Glacier Instant Retrieval
- S3 Glacier Flexible Retrieval - 최대 1시간
- S3 Glacier Deep Archive - 최대 12시간

### 접근 빈도 불규칙. 자동 조정
- S3 Intelligent-Tiering


## 즉시 조회 여부

### 즉시 조회 가능
- S3 Standard
- S3 Standard-IA
- S3 One Zone-IA
- S3 Glacier Instant Retrieval
- S3 Intelligent-Tiering

### 조회 시 시간 소요
- S3 Glacier Flexible Retrieval - 최대 1시간
- S3 Glacier Deep Archive - 최대 12시간


>Glacier
>`Glacier` 스토리지 클래스는 **법/감사/규정** 목록으로 장기 보관할 때 사용함.
>이 목적이 아닌데, 거의 접근하지 않는다 -> **S3 Standard-IA** 고르자.


# S3 버전 관리, 객체 잠금, 수명 주기 정책

기본 -> 파일 중복 업로드시 파일 덮어 씌워짐. -> 기존 파일 삭제됨.
이를 방지하려면 **버전 관리** 기능을 활성화 시켜야 함.

## S3 객체 잠금
일정 기간 동안 파일의 일정 기간 동안 파일의 수정/삭제를 차단하는 기능.

#### 거버넌스 모드
- 특별 권한이 있는 관리자만 수정/삭제 가능 (다른 사용자는 수정/삭제 불가)
#### 규정 준수 모드
- 모든 사용자가 수정/삭제 불가능 (루트 사용자조차도 수정/삭제 불가능)


#### 법적 보존 (보조 기능)
- 기간에 상관없이 수동으로 해제하기 전까지 객체의 수정/삭제를 금지하는 기능
- 언제 끝날지 모르는 소송과 같은 이슈가 발생했을 때 사용

## S3 수명 주기 정책

파일을 N일 후 자동으로 이동/삭제 시키는 기능
- 데이터 접근 빈도를 예측할 수 있어서 다른 유형의 S3로 이동하고 싶을 때나 보관 기간이 정해져 보관 기간 이후에 파일을 삭제하고 싶을 때 주로 사용


# S3 암호화 - SSE, S3 Batch Operations

## SSE (Server Side Encryption)

SSE는 서버 자체적으로 암호화하는 방식을 의미함.
- 암호화할 때는 키가 필요함.

#### SSE 종류
1. **SSE-S3**: S3가 키를 **알아서** 생성 및 관리하는 방식
	- 가장 기본적이고 관리가 쉬움
2. **SSE-KMS**: 암호화할 때 사용하는 키를 생성 및 관리해주는 방식
	- 철저한 보안 요구 시 이 방식을 주로 사용함
	- **AWS KMS**: 암호화할 때 사용하는 키를 생성 및 관리해주는 **서비스**
		- KMS는 암호화 키를 주기적으로 **자동 교체**해주는 편리한 방식임
	- KMS를 쓰면 S3에 저장된 파일마다 키를 **별도로** 생성해서 암호화 진행함.
		- 따라서 파일이 많으면 비용이 많이 나옴.
		- 하지만 **S3 Bucket Key**라는 것을 활용하면 파일마다 별도 키를 생성하지 않고 Bucket Key를 **재사용**하기에 암호화 비용 절감 가능
3. **SSE-C**: 고객이 키를 직접 생성 및 관리하는 방식
	- 고객이 키를 관리하는 게 번거롭고 위험해서 권장 X

## S3 Batch Operations

S3에 저장된 수백만 ~ 수십억 개의 파일에 대해 **동일한 작업(복사, 삭제, 설정 적용 등)을** 한 번에 실행할 수 있게 해주는 서비스.


# EBS, EFS, FSx, 인스턴스 스토어

## EBS (Elastic Block Store)

EBS는 외장 SSD/HDD처럼 EC2에 연결해서 사용하는 블록 스토리지 서비스
- EBS는 EC2, RDS를 제외한 다른 AWS 서비스에는 연결해서 사용할 수 없음
- EBS는 **단일 AZ**에서만 작동함.
- 고성능 스토리지로 사용할 수 있는 유형이 존재함()

## EFS (Elastic File System)

EFS는 여러 대의 컴퓨터가 동시에 같은 파일 시스템을 공유해서 쓸 수 있는 NFS(Network File System) 스토리지
- 일종의 구글 클라우드나 iCloud 같은 것.
- 동시에 여러 사용자가 같은 파일 시스템을 공유해서 쓰는 방식

- EFS는 **다중 AZ**에서 작동할 수 있음
- 고성능 스토리지는 아님
- NFS 프로토콜만 지원함
- S3의 Intelligent-Tiering 기능처럼 자주 접근하지 않는 파일을 EFS IA(Infrequent Access) 스토리지 클래스로 이동시켜주는 EFS Intelligent-Tiering 기능도 존재함.
	- EFS IA 스토리지 클래스로 이동한 파일이라도 즉시 접근이 가능함

# 인스턴스 스토어 (Instance Stroe)

인스턴스 스토어는 EC2 컴퓨터에 내장되어 있는 임시용 디스크.
- EC2 컴퓨터에 내장된 디스크이다보니, EC2 인스턴스를 중지하거나 종료하면 데이터가 전부 사라짐.

## FSx (File Sytstem for Extended use)

FSx는 고성능(높은 처리량, 낮은 지연 시간) 파일 스토리지 서비스

- FSx for Lustre
	- 머신러닝, 빅데이터 분석 시 자주 활용
	- S3와 연동해서 사용 가능
	- Lustre 자체 프로토콜만 지원

- FSx for NetApp ONTAP
	- 다양한 운영체제(윈도우, 맥, 리눅스)에 호환
	- NFS, SMB 프로토콜 둘 다 지원.
		- NFS: 리눅스/유닉스 시스템에서 사용하는 파일 공유 프로토콜
		- SMB: Windows에서 사용하는 파일 공유 프로토콜

- FSx for Windows File Server
	- SMB 프로토콜만 지원

- FSx for OpenZFS
	- NFS 프로토콜만 지원