**차수(degree)**
- 노드의 차수: 노드에 연결된 자식 노드의 수
- 트리의 차수: 트리에 있는 노드의 차수 중에서 가장 큰 값

**높이**
- 노드의 높이: 루트에서 노드에 이르는 간선의 수 (노드의 레벨)
- 트리의 높이: 트리에 있는 노드의 높이 중에서 가장 큰 값 (최대 레벨)

**이진 트리**
- 높이 i에서의 노드의 최대 개수는 $2^i$ -> 1, 2, 4, 8 ...
- 높이가 h인 이진 트리가 가질 수 있는 노드의 최소 개수는 ($h+1$), 최대 개수는 ($2$$^h$$^+$$^1$$-1$)개가 됨.

**정 이진 트리**
- 모든 노드의 차수가 0이거나 2인 이진 트리

**포화 이진 트리**
- 모든 레벨에 노드가 포화 상태로 차있는 이진 트리
- 높이가 h일 때, 최대 노드의 개수인 ($2$$^h$$^+$$^1$ $- 1$)의 노드를 가진 이진 트리

**완전 이진 트리**
- 높이가 h이고 노드의 수가 n개일 때, 마지막 레벨을 제외하고 모든 레벨이 꽉 차있음과 동시에 마지막 레벨에서는 왼쪽부터 빼곡히 채워진 형태의 이진 트리

**편향 이진 트리**
- 높이 h에 대한 최소 개수의 노드를 가지면서 한쪽 방향의 자식 노드 만을 가진 이진 트리

# 시험 각
**전위순회(preorder taversal)**
- V L R
- 부모 노드 방문 후 자식 노드를 좌, 우 순서로 방문

**중위순회(inorder traversal)**
- L V R
- 왼쪽 자식 노드, 부모 노드, 오른쪽 자식 노드 순으로 방문

**후위순회(postorder traversal)**
- L R V
- 자식 노드를 좌, 우 순서로 방문한 후 부모 노드로 방문

전위 중위 후위라는 말이, 부모 노드의 방문 순서를 일컫는 말이니까 그걸 기억하면 됨.


**최대 힙(max heap)**
- 키 값이 가장 큰 노드를 찾기 위한 완전 이진 트리
- 부모 노드의 키 값 >= 자식 노드의 키 값
- 루트 노드: 키 값이 가장 큰 노드

**최소 힙(min heap)**
- 키 값이 가장 작은 노드를 찾기 위한 완전 이진 트리
- 부모 노드의 키 값 <= 자식 노드의 키 값
- 루트 노드: 키 값이 가장 작은 노드


# 시험 각

| 개념   | 정의                        | 순서 고려 여부 | 선택 개수 제한 | 경우의 수 (개수)                           |
| ---- | ------------------------- | -------- | -------- | ------------------------------------ |
| 부분집합 | 원소들 중 0개 이상 선택한 모든 가능한 집합 | 무시       | 없음       | $2^n$                                |
| 조합   | n개 중 k개를 순서 없이 선택         | 무시       | k개 선택    | $\binom{n}{k} = \frac{n!}{k!(n-k)!}$ |
| 순열   | n개 중 k개를 순서 있게 나열         | 고려       | k개 선택    | $P(n,k) = \frac{n!}{(n-k)!}$         |

|순회|방문 순서 특징|주된 용도|
|---|---|---|
|전위|루트 먼저 방문|트리 구조 저장, 복원, 직렬화|
|중위|루트가 가운데, 정렬된 결과|BST 정렬 출력, 중위 표기법 수식 표현|
|후위|루트 마지막 방문|리소스 해제, 후위 표기법 계산|

---


---

# 파리퇴치
```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
	
	static BufferedReader br;
	static StringTokenizer st;
	
	public static void main(String[] args) throws IOException {
		br = new BufferedReader(new InputStreamReader(System.in));
		
		int T = Integer.parseInt(br.readLine());
		
		for (int test_case = 1; test_case <= T; test_case++) {
			st = new StringTokenizer(br.readLine());
			int N = Integer.parseInt(st.nextToken());
			int M = Integer.parseInt(st.nextToken());
			
			int[][] arr = new int[N][N];
			
			for (int i = 0; i < N; i++) {
				st = new StringTokenizer(br.readLine());
				for (int j = 0; j < N; j++) {
					arr[i][j] = Integer.parseInt(st.nextToken());
				}
			}
			
			int maxSum = Integer.MIN_VALUE;
			
			for (int i = 0; i <= N - M; i++) {
				for (int j = 0; j <= N - M; j++) {
					int sum = 0;
					for (int y = 0; y < M; y++) {
						for (int x = 0; x < M; x++) {
							sum += arr[i + y][j + x];
						}
					}
					maxSum = Math.max(maxSum, sum);
				}
			}
			
			System.out.println("#" + test_case + " " + maxSum);
		}
	}
}

```

---

# 햄버거 다이어트
```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

import org.omg.CORBA.INTERNAL;

public class Solution {

	static BufferedReader br;
	static StringTokenizer st;
	static StringBuilder sb;
	static int N, L;
	static int[] michelinScore;
	static int[] kcal;
//	static boolean[] ate;
	static int curKcal;
	static int curMicehlinScore;
	static int maxMichelinScore;
	
	public static void main(String[] args) throws IOException {
		br = new BufferedReader(new InputStreamReader(System.in));
		
		int T = Integer.parseInt(br.readLine());
		
		for (int test_case = 1; test_case <= T; test_case++) {
			
			curKcal = 0;
			curMicehlinScore = 0;
			maxMichelinScore = Integer.MIN_VALUE;
			 
			st = new StringTokenizer(br.readLine());
			
			N = Integer.parseInt(st.nextToken());
			L = Integer.parseInt(st.nextToken());
			
			michelinScore = new int[N];
			kcal = new int[N];
//			ate = new boolean[N];
			
			for (int i = 0; i < N; i++) {
				st = new StringTokenizer(br.readLine());
				michelinScore[i] = Integer.parseInt(st.nextToken());
				kcal[i] = Integer.parseInt(st.nextToken());
			}
			
			hambugi(0);
			
			sb = new StringBuilder().append("#").append(test_case).append(" ").append(maxMichelinScore);
			System.out.println(sb);
		}

	}

	// 순열 버전
//	private static void hambugi(int eatingCnt) {
//		if (curKcal > L) return;
//		
//		if (eatingCnt == N) {
//			// 다 먹어도 제한 칼로리 미만이면 그게 최대값
//			maxMichelinScore = Math.max(maxMichelinScore, curMicehlinScore);
//			return;
//		}
//		
//		maxMichelinScore = Math.max(maxMichelinScore, curMicehlinScore);
//		
//		for (int i = 0; i < N; i++) {
//			if (ate[i]) continue;
//			
//			ate[i] = true;
//			curKcal += kcal[i];
//			curMicehlinScore += michelinScore[i];
//
//			hambugi(eatingCnt + 1);
//			
//			ate[i] = false;
//			curKcal -= kcal[i];
//			curMicehlinScore -= michelinScore[i];
//		}
//		
//	}
	
	private static void hambugi(int eatingIdx) {
		if (curKcal > L) return;
		
		maxMichelinScore = Math.max(maxMichelinScore, curMicehlinScore);
		
		for (int i = eatingIdx; i < N; i++) {
			curKcal += kcal[i];
			curMicehlinScore += michelinScore[i];
	
			hambugi(i + 1);
			
			curKcal -= kcal[i];
			curMicehlinScore -= michelinScore[i];
		}
	}
}

```

---

# 수제 버거 장인
```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.lang.Character.Subset;
import java.util.StringTokenizer;

public class Solution {
	
	static int N;
	static int M;
	static StringBuilder sb;
	static boolean[] isUsed;
	static boolean[][] hambugiProhibit; // 금지된 햄부기 조합
//	static int[] hambugiIndex;
	static int ans;
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		
		int T = Integer.parseInt(br.readLine());
		
		for (int test_case = 1; test_case <= T; test_case++) {
			sb = new StringBuilder();
			StringTokenizer st = new StringTokenizer(br.readLine());
			
			ans = 0;
			N = Integer.parseInt(st.nextToken());
			M = Integer.parseInt(st.nextToken());
			
			isUsed = new boolean[N + 1];
			hambugiProhibit = new boolean[N + 1][N + 1];
			
			if (M == 0) {
				int ans = 1 << N;
				sb.append("#").append(test_case).append(" ").append(ans);
				System.out.println(sb);
				continue;
			}
			
			for (int i = 1; i <= M; i++) {
				st = new StringTokenizer(br.readLine());
				int A = Integer.parseInt(st.nextToken());
				int B = Integer.parseInt(st.nextToken());
				hambugiProhibit[A][B] = true;
				hambugiProhibit[B][A] = true;
			}
			
			subset(1);
			
			sb.append("#").append(test_case).append(" ").append(ans);
			System.out.println(sb);
		}
	}

	private static void subset(int idx) {
		boolean flag = false;
		
		if (idx == N + 1) {
			for (int i = 1; i <= N; i++) {
		        if (!isUsed[i]) continue;
		        for (int j = i + 1; j <= N; j++) {
		        	if (!isUsed[j]) continue;
		            if (hambugiProhibit[i][j]) {
		            	return;
		            }
		        }
		    }
			ans++;
			return;
		}
		
	    // idx번째 재료를 사용해도 되는지 체크
	    boolean canUse = true;
	    for (int i = 1; i < idx; i++) {
	        if (isUsed[i] && hambugiProhibit[i][idx]) {
	            canUse = false;
	            break;
	        }
	    }
	    
	    // idx번째 재료를 사용하는 경우
	    if (canUse) {
	        isUsed[idx] = true;
	        subset(idx + 1);
	    }
	    
	    // idx번쨰 재료를 사용하지 않는 경우
	    isUsed[idx] = false;
	    subset(idx + 1);
	    
	}
}

```

---

# Ladder1
```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Solution {
	
	public static class Pair {
		int x;
		int y;
		
		public Pair(int x, int y) {
			this.x = x;
			this.y = y;
		}
	}
	
	static int[] dx = {-1, 1, 0};
	static int[] dy = {0, 0, -1};

	static int[][] arr;
	static Queue<Pair> q = new LinkedList<>();
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		for (int test_case = 1; test_case <= 10; test_case++) {
			int T = Integer.parseInt(br.readLine());
			StringBuilder sb = new StringBuilder();
			
			arr = new int[100][100];
			
			for (int i = 0; i < 100; i++) {
				StringTokenizer st = new StringTokenizer(br.readLine());
				for (int j = 0; j < 100; j++) {
					arr[i][j] = Integer.parseInt(st.nextToken());
					// 시간 초과 난다면 -> 가로 사다리 위치를 3과 같은 수로 만들 필요도 있을 듯
//					if (j > 0 && j < 99 && arr[i][j - 1] == 1) {
//						arr[i][j - 1] = 3;
//					}
				}
			}
			
			for (int i = 0; i < 100; i++) {
				if (arr[99][i] == 2) {
					q.add(new Pair(i, 99));
					Pair ans = bfs();
					sb.append("#");
					sb.append(test_case);
					sb.append(" ");
					sb.append(ans.x);
				}
			}
			
			System.out.println(sb);
		}

	}

	private static Pair bfs() {
		
		while (!q.isEmpty()) {
			Pair cur = q.poll();

			for (int dir = 0; dir < 3; dir++) {
				int nx = cur.x + dx[dir];
				int ny = cur.y + dy[dir];
				
				if (nx < 0 || nx >= 100) continue;
				if (ny < 0) {
					return new Pair(cur.x, cur.y);
				}
				if (arr[ny][nx] == 0) continue;
				
				q.add(new Pair(nx, ny));
				arr[cur.y][cur.x] = 0;
				break;
			}
		}
		return null;
	}
}


```


---

# 결혼식
```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

    static boolean[][] network;
    static boolean[] visited;
    static int[] depth;
    
    public static void main(String[] args) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int N = Integer.parseInt(br.readLine());
        int M = Integer.parseInt(br.readLine());
        
        network = new boolean[N + 1][N + 1];
        visited = new boolean[N + 1];
        depth = new int[N + 1];

        for (int i = 0; i < M; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            network[a][b] = true;
            network[b][a] = true;
        }

        Queue<Integer> q = new LinkedList<>();
        
        q.add(1);
        visited[1] = true;

        int inviteCnt = 0;

        while (!q.isEmpty()) {
            int cur = q.poll();

            for (int i = 1; i <= N; i++) {
                if (!visited[i] && network[cur][i]) {
                    depth[i] = depth[cur] + 1;
                    if (depth[i] <= 2) {
                        inviteCnt++;
                        visited[i] = true;
                        q.add(i);
                    }
                }
            }
        }

        System.out.println(inviteCnt);
    }
}

```

---

# 효율적인 해킹
구현은 성공, 시간 초과가 문제
```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br;
	static StringTokenizer st;
	static StringBuilder sb;
	
	static int N, M;
	static ArrayList<Integer>[] graph;
	static int[] hackingCnt;

    public static void main(String[] args) throws IOException {
        
        br = new BufferedReader(new InputStreamReader(System.in));
        sb = new StringBuilder();
        
        st = new StringTokenizer(br.readLine());
        
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        
        graph = new ArrayList[N + 1];
        hackingCnt = new int[N + 1];
        
        for (int i = 1; i <= N; i++) {
        	graph[i] = new ArrayList<>();
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            
            int a = Integer.parseInt(st.nextToken()); 
            int b = Integer.parseInt(st.nextToken());
            
            graph[b].add(a);
        }
        
        for (int i = 1; i <= N; i++) {
            boolean[] visited = new boolean[N + 1];
            
            Queue<Integer> q = new LinkedList<>();
            
            q.add(i);
            visited[i] = true;
            int count = 0;

            while (!q.isEmpty()) {
                int cur = q.poll();
                for (int next : graph[cur]) {
                    if (!visited[next]) {
                        visited[next] = true;
                        q.add(next);
                        count++;
                    }
                }
            }

            hackingCnt[i] = count;
        }

        int maxCnt = 0;
        for (int i = 1; i <= N; i++) {
            if (hackingCnt[i] > maxCnt) {
            	maxCnt = hackingCnt[i];
            }
        }
   
        for (int i = 1; i <= N; i++) {
            if (hackingCnt[i] == maxCnt) {
            	sb.append(i).append(" ");
            }
        }

        System.out.println(sb);
    }
}

```

# 8월 평가


## 과목 평가 - Front



### CSS
`!important`
- 우선 적용되어야 하는 속성

**명시도**
- X: ID 선택자의 개수
- Y: 클래스 선택자, 속성 선택자, 가상 클래스 선택자 개수
- Z: 타입 선택자, 가상 요소 선택자 개수

1. e-book (CSS 1 / 28 - 37 페이지)
box model 읽어볼것
- 텍스트, 이미지 등의 모든 콘텐츠를 사각의 박스 형태로 관리하는 모델
- block 요소는 위, 아래로, inline 요소는 왼쪽에서 오른쪽으로 배치됨.
- box는 content, padding, boreer, margin 등으로 구성됨.
- width, height, ... minwidth minheight ... 등등
- block 요소는 width와 height를 갖지만 inline 요소는 무시됨
- margin: (상하 좌우) 또는 (상 좌우 하) 또는 (상 우 하 좌)

(1) 34페이지
   box-sizing: content-box는 width/height가 콘텐츠 영역만 계산한다.
   - content-box 
	   - 전체 크기 : (가로 + padding + border), (세로 + padding + border)
	   - 콘텐츠 영역: 지정한 가로, 세로
   - border-box 
	   - 전체 크기 : 지정한 가로, 세로
	   - 콘텐츠 영역 : (가로 - padding - border), (세로 - padding - border)

(2) 28페이지
   content+padding+border의 높이 구하는 방법
   - content-box : (가로 + padding + border), (세로 + padding + border)
   - border-box : 지정한 가로, 세로
---------------------------------------------------------
2. e-book (CSS 2 / 13, 15 페이지)
(1) flex container에게 적용되는 속성
    ex) display / flex-direction / flex-wrap 등 설명 읽어볼것
(2) flex item에 적용되는 속성
    ex) flex-grow / flex-shrink 등 설명 읽어볼것
-----------------------------------------------------------
3. e-book (CSS 2 / 20-24 페이지)
position ==> static, relative, absolute, fiexd 정리
----------------------------------------------------------
4. 반응형 레이아웃을 위해 사용되는 HTML 메타 태그는 
<meta name="viewport" content="width=device-width, initial-scale=1.0">

이 태그는 사용자의 기기 화면 크기에 맞게 웹사이트의 레이아웃을 동적으로 조정하도록 브라우저에 지시한다.


### JavaScript

1.   e-book (Ajax / 4페이지)
Ajax의 개념정리 할것(지문을 주고 이게 뭐냐?? 라고 주관식으로 물어볼수 있음)

- 비동기로 처리되는 JavaScript와 XML (요새는 JSON이긴 하지만.)
- 화면 갱신 없이 클라이언트와 서버간에 데이터 등 정보를 교환할 때 주로 사용

동기와 비동기의 차이
- 동기는 순차적 실행
	- 또한 단일 작업
	- 위에서 아래로
- 비동기는 병렬적 실행
	- 다중작업
	- 콜백 함수나 프로미스 등을 통해서


----------------------------------------------------------
2. 시스템이 호출하는 함수: 콜백(callback)함수
----------------------------------------------------------
3.  e-book (Ajax / 15, 17 페이지)
비동기 통신 async/await와 Promise.then()에 대해 찾아보고 정리할것(차이점/장단점등 서술형으로 엄청 잘 나옴)

----------------------------------------------------------
4. e-book (JavaScript 2 / 26,27 페이지)
webStorage의 종류에 대해 정리하고, Storage API도 정리하세요
   (1) sessionStorage
   (2) localStorage
----------------------------------------------------------
5. e-book (JavaScript 2 / 30 페이지)
객체직렬화/ 역직렬화 설명과 함수
----------------------------------------------------------
6. 기타
코드를 실행했을때 결과가 뭐냐? 
(콜백함수가 실행된 후의 결괏값 등)

## 월말 평가 - 알고리즘


