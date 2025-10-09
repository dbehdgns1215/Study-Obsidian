STS = 오전 자바 라이브
이클립스 = 오후 알고리즘 라이브

TODO (git_repository 디렉토리)
![[Pasted image 20250721164510.png]]
- 자바 라이브 과제
	-  제출법
		- `project.ssafy.com`
	- 과제 내용
		- LV 3 문제 1개씩
		- 과제 문제 1개씩
	- `homework\` -> project.ssafy.com에서 clone 뜨기
		- 각 문제 들어가서 `실습하기` 후 깃랩 주소 복사
- 자바 알고리즘 라이브 과제
	- 제출법
		- `C:SSAFY/git_repository/algo_homework/오늘날짜/`
		- 오늘 날짜 폴더 및 파일 생성해서 과제 진행
		- `git add .`
		- `git commit -m "알고 과제"`
		- `git push origin master`
		- 추가로 MM에 `답글달기`로 `메모리, 시간, 전략` + `코드 파일`
	- `algo_homework\` -> lab.ssafy.com에서 clone 뜨기
		- `https://lab.ssafy.com/dbehdgns1215/homework`
	- 집에서
		- `D:\SSAFY\algo_homework` -> `git bash 열기` -> `git pull https://lab.ssafy.com/dbehdgns1215/homework.git master` pull 땡겨오기 
- 자바 라이브
	- `live\` -> 어디선가 가져왔음
- 알고리즘 라이브
	- `algorithm\` -> lab.ssafy.com에서 clone 뜨기
		- `git clone https://lab.ssafy.com/s14/java/algorithm_live.git`
		- 매일 라이브 진행 이후 또는 이전에 미리 pull 받아야 함


- MM에 있는 파일 `IM 대비.pdf` - IM 검정 대비 필수 문제 20선
	- https://jungol.co.kr/ - 정올
	- 백준
	- SWEA

- A형 대비
	- BOJ - 게리맨더링
	- SWEA - 나무 높이

- 집에서 알고 이클립스 실행
```
eclipse.ini파일 안에 아래 내용 추가

✨ 위치 : --launcher 아래 -vmargs 위에 즉, 둘 사이의 위치에 설정할 것    
📖 내용 
    -vm
    C:\Program Files\Zulu\zulu-8\bin // 경로 확인 필요
```
- Zulu
	- SW검정 폴더 내에 있는 파일
- eclipse 2018-09
	- SW검정 폴더 내에 있는 파일
- STS
	- sts-4.22.1.RELEASE

- Utils
	- algo_submit - SWEA, 백준 코드 자동 변경
	- SWEA COPYPASTA - 예제 입력 출력을 버튼 하나로



과평 32문제
- 객관식 21
- 주관식 11
	- 단답 9
	- 서술 2


월말 5문제
- 별찍기, 배열 속 최소 최대 찾기
- 빌딩건설처럼 2차원 배열 탐색하는 문제
- 스택, 큐, 리스트 이런거 쓰는 문제
- 부분 점수 테케 맞으면 절반, 히든 테케 맞아야 만점


---

2회차 과목평가 - 알고리즘

- 서술형 문제
	- 3개 정도 서술. 특정 개념 보고 간단한 설명 및 예시 설명
	- 아마 전위 중위 후위?
	- 순, 조, 부
	- 트리 쪽 잘 보면 될듯
- 알고리즘
	- 한 문제는 2차원 배열에서 왔다갔다
	- 나머지 두개는 알고리즘 써야함
		- 순열 조합 부분집합




# 자리 옮기고 옵시디언 세팅
```cmd
git clone 옵시디언
-> 클론 뜬 폴더를 볼트로 옵시디언 실행

C:\Users\SSAFY>git config --list --show-origin
C:\Users\SSAFY>git config --global user.email "dbehdgns1215@naver.com"
C:\Users\SSAFY>git config --global user.name "dbehdgns1215"
C:\Users\SSAFY>git config --list --show-origin
```