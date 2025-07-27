
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

- Q2를 도입 안하고 하나의 큐로 이용한다면, 경로가 겹쳤을 때 dist를 어떻게 갱신해야하지?
	- 그래서 탐색이 끝났을 때, 벽 만난 지점부터 다시 BFS를 다른 경로로 돌린다면 -> 이게 n^3인데???? 그럼 이건 패스
	- Q를 먼저 진행시키고 dist가 다 나온 상태일 때, Q2에 있는 걸 다시 Q에 넣어서 진행시키다가 dist가 더 작으면 갱신해준다

	- Node(int x, int y, int cost) {...}
	- 좌표쌍과 우선순위를 도입해서 BP에서 길을 부술 때마다 cost를 증가 시켜서 큐에 삽입
		- 따라서 cost가 작은 것들부터 출력하고 BP에서 길을 안부순 세계선을 다시 진행 시키면 이게 n^3이 아닌가?????????????

그러면 board 있어야하고 dist 있어야하고 얼리 리턴 조심
```


## BOJ_2206 - 벽 부수고 이동하기
```memo
if (board[ny][nx] == 1 && wallBreakCnt == 0) {
	Q.add... // 큐에 현재 좌표 넣고
	BFS 계속 진행
	wallBreakCnt++;
}

if (board[ny][nx] == 1 && wallBreakCnt == 1) {
	wallBreakCnt--;
	continue;
}

} // BFS 끝

1. 
벽을 만났을 때, 해당 좌표를 Q2에 넣어서 부순 포인트를 가지고 있다가
기존 Q의 진행이 끝나서 dist가 다 갱신된 상태일 때, Q2에 있는 걸 다시 Q에 넣고 다시 진행. -> dist가 더 작으면 갱신.

2. 
- Node(int x, int y, int cost) {...}
- 좌표쌍과 우선순위를 도입해서 BP에서 길을 부술 때마다 cost를 증가 시켜서 큐에 삽입
	- 따라서 cost가 작은 것들부터 출력하고 BP에서 길을 안부순 세계선을 다시 진행 시키면 이게 n^3이 아닌가?????????????
```


## BOJ_10798 - 세로읽기
```java
package study;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ_10798 {
	
	static String[] lines;
	static StringBuilder sb;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		lines = new String[5];
		int maxLen = 0;

		for (int i = 0; i < 5; i++) {
			lines[i] = br.readLine();
			maxLen = Math.max(maxLen, lines[i].length());
		}

		sb = new StringBuilder();


		for (int j = 0; j < maxLen; j++) {
			for (int i = 0; i < 5; i++) {
				if (j < lines[i].length()) { // **.length() -> 길이 반환 -> idx 사용 시에는 -1 해야함을 명심 (Zero-Index) -> 가능한 경우 j(idx: 2) < 길이 3(idx: 2) / 불가능 j(idx: 2) < 길이 2(idx: 1)
					sb.append(lines[i].charAt(j));
				}
			}
		}

		System.out.println(sb);
	}
}
```
- `if (j < lines[i].length())`
	- 2차원 배열의 관점에서 고정관념을 조금 깨야 할 필요가 있음.
	- 왜 `j`랑 `lines[i].length()`를 비교하는지 생각해볼 것.
		- `j` 값에 따라서 해당 라인에 문자를 출력할 수 있는지 없는지 확인
```input
  j|012345
i|0	AABCDD
  1	afzz
  2	09121
  3	a8EWg6
  4	P5h3kx
```
