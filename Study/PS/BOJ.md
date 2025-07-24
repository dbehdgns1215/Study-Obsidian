
## BOJ_2206 - 벽 부수고 이동하기 \[G3]
```memo
if (board[ny][nx] == 1 && wallBreakCnt == 0) {
	Q2.add... // 큐에 현재 좌표 넣고
	BFS 계속 진행
	wallBreakCnt++;
}

if (board[ny][nx] == 1 && wallBreakCnt == 1) {
	wallBreakCnt--;
	continue;
}

} // BFS 끝

- 탐색이 끝났을 때, Q2에 있는 BP 부터 다시 BFS를 시작? -> 사실상 n^3이 아닌가?
- 
- Q2를 도입 안하고 하나의 큐로 이용한다면, 경로가 겹쳤을 때 dist를 어떻게 갱신해야하지?
	- 그래서 탐색이 끝났을 때, 벽 만난 지점부터 다시 BFS를 다른 경로로 돌린다면 -> 이게 n^3인데???? 그럼 이건 패스
	- Q를 먼저 진행시키고 dist가 다 나온 상태일 때, Q2에 있는 걸 다시 Q에 넣어서 진행시키다가 dist가 더 작으면 갱신해준다

	- Node(int x, int y, int cost) {...}
	- 좌표쌍과 우선순위를 도입해서 BP에서 길을 부술 때마다 cost를 증가 시켜서 큐에 삽입
		- 따라서 cost가 작은 것들부터 출력하고 BP에서 길을 안부순 세계선을 다시 진행 시키면 이게 n^3이 아닌가?????????????

그러면 board 있어야하고 dist 있어야하고 얼리 리턴 조심
```
