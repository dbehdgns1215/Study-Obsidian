

![[Pasted image 20250721160309.png]]

**Pair in Java**
```java
static class Pair {
	int x, y;
	
	public Pair(int x, int y) {
		this.x = x;
		this.y = y;
	}
}
```



# List Interface
- ArrayList: `List<자료형> arrayList = new ArrayList<>()`
- LinkedList:  `List<자료형> linkedList = new LinkedList<>()`
- Stack (권장 X)
- Vector (권장 X)


```text
Collection<E> (인터페이스)
├── List<E>
│   ├── ArrayList<E>
│   └── LinkedList<E>
│
├── Queue<E>
│   ├── LinkedList<E>
│   └── ArrayDeque<E>
│
└── Set<E>
    ├── HashSet<E>
    ├── LinkedHashSet<E>
    └── TreeSet<E>

Map<K, V> (인터페이스)
├── HashMap<K, V>
├── LinkedHashMap<K, V>
└── TreeMap<K, V>
```

```java
// ========== List 계열 ==========
List<Integer> li = new ArrayList<>();
List<Integer> li = new LinkedList<>();

// ========== Queue 계열 ==========
Queue<Integer> q = new LinkedList<>();
Queue<Integer> q = new ArrayDeque<>();

// ========== Deque 계열 ==========
Deque<Integer> dq = new LinkedList<>();
Deque<Integer> dq = new ArrayDeque<>();

// ========== Set 계열 ==========
Set<Integer> s = new HashSet<>();
Set<Integer> s = new LinkedHashSet<>();
Set<Integer> s = new TreeSet<>();

// ========== Map 계열 ==========
Map<String, Integer> m = new HashMap<>();
Map<String, Integer> m = new LinkedHashMap<>();
Map<String, Integer> m = new TreeMap<>();

// ========== Stack (Deque로 구현 권장) ==========
Deque<Integer> s = new ArrayDeque<>();   // 추천

// ========== PriorityQueue (Queue의 서브타입) ==========
Queue<Integer> minHeap = new PriorityQueue<>();
Queue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());
```

# Day 10

## Tree
- 비선형 구조
- 원소들간에 `1:n` 관계를 가지는 자료구조
- 원소들 간에 계층 관계를 가지는 계층형 자료구조
- 상위 원소에서 하위 원소로 내려가면서 확장되는 트리(나무)모양의 구조
	- 브랜치 노드
	- 리프  노드

### 노드(node) - 트리의 원소
- 한 개 이상의 노드로 이루어진 유한 집합이며 다음 조건을 만족한다.
	- 노드 중 최상위 노드를 루트라고 한다.
	- 나머지 노드들은 n (n >= 0) 개의 분리 집합 T$1$, ..., T$_N$으로 분리될 수 있다.
- 이들 T$_1$, ..., T$N$은 각각 하나의 트리가 되며(재귀적 정의) 루트의 부 트리(subtree)라 한다.

### 간선(edge) - 노드와 노드를 연결하는 선
- 부모 노드와 자식 노드를 연결


![[Pasted image 20250804142113.png]]
### 루트 노드(root node) - 트리의 시작 노드인 최상위 노드
- 트리 T의 루트 노드 - A

### 형제 노드(sibling node) - 같은 부모 노드의 자식 노드들
- B, C, D는 형제 노드
- E, F는 형제 노드
- K는 형제 노드
### 조상 노드 - 간선을 따라 루트 노드까지 이르는 경로에 있는 모든 노드들
- K의 조상 노드: F, B, A
### 서브 트리(subtree) - 부모 노드와 연결된 간선을 끊었을 때 생성되는 트리

### 자손 노드 - 서브 트리에 있는 하위 레벨의 노드들
- B의 자손 노드: E, F, X



![[Pasted image 20250804142729.png]]

## 차수(degree)
- 노드의 차수: 노드에 연결된 자식 노드의 수 (B의 차수 = 2, C의 차수 = 1)
	- `자식 노드로의 간선 수`
- 트리의 차수: 트리에 있는 노드의 차수 중에서 가장 큰 값 (트리 T의 차수 = 3)
	- `max(노드의 차수들) => 트리의 차수`
- 단말 노드(리프 노드): 차수가 0인 노드 즉, 자식 노드가 없는 노드

>참고
>이진트리: 트리의 차수가 오직 `2`인 트리
## 높이
- 노드의 높이: 루트에서 노드에 이르는 간선의 수. (B의 높이 = 1, F의 높이 = 2)
- 트리의 높이: 트리에 있는 노드의 높이 중에서 가장 큰 값. 최대 레벨 (트리 T의 높이 = 3)


## 이진 트리
- 모든 노드의 최대 차수를 2로 제한
- 각 노드가 자식 노드를 최대한 2개 까지만 가질 수 있는 트리
	- 왼쪽 자식 노드 (left child node)
	- 오른쪽 자식 노드 (right child node)
- 모든 노드들이 최대 2개의 서브 트리를 갖는 특별한 형태의 트리
- 이진 트리의 예
![[Pasted image 20250804143634.png]]

### 높이 i(레벨 i)에서의 노드의 최대 개수
- 바로 2$^i$ 개
![[Pasted image 20250804143827.png]]
- 높이가 h인 이진 트리가 가질 수 있는 노드의 최소 개수는 (h + 1)개가 되며, 최대 개수는 2($^h$ $^+$ $^1$ - 1)개가 된다.

## 정 이진 트리 (Full Binary Tree)
- 모든 노드의 차수가 0이거나 2인 이진 트리
![[Pasted image 20250804144239.png]]

## 포화 이진 트리 (Perfect Binary Tree)
- 모든 레벨의 노드가 포화 상태로 차있는 이진 트리
- 높이가 h일 때, 최대 노드의 개수인 (2$^h$$^-$$^1$ - 1)의 노드를 가진 이진 트리
	- 높이 3일 때 2$^3$$^+$$^1$ - 1 = 15개의 노드
- 루트를 1번으로 하여 2$^h$$^+$$^1$ -1 까지 정해진 위치에 대한 노드 번호를 가짐
![[Pasted image 20250804145523.png]]

## 완전 이진 트리 (Complete Binary Tree)
- 높이가  N이고 노드 수가 N개 일 때, (단, h + 1 <= n < 2$^h$$^+$$1$) 포화 이진 트리의 노드 번호 1번부터 n번까지 빈 자리가 없는 이진 트리
- 예) 노트가 10개인 완전 이진 트리
![[Pasted image 20250804145510.png]]


## 편향 이진 트리 (Skewed Binary Tree)
- 높이 h에 대한 최소 개수의 노드를 가지면서 한쪽 방향의 자식 노드만을 가진 이진 트리
	- 왼쪽 편향 이진 트리
	- 오른쪽 편향 이진 트리
![[Pasted image 20250804145448.png]]


## 배열을 이용한 이진 트리의 표현
![[Pasted image 20250804151638.png]]

![[Pasted image 20250804151544.png]]

![[Pasted image 20250804151552.png]]
- 0번 인덱스 비우고 노드의 번호를 배열의 인덱스로 해서 생성

**배열을 이용한 이진 트리의 표현의 단점**
- 편향 이진 트리의 경우에 사용하지 않는 배열 원소에 대한 메모리 낭비 발생
- 트리의 중간에 새로운 노드를 삽입하거나 기존의 노드를 삭제할 경우 배열의 크기 변경 어려움

## 비선형 자료구조 탐색
![[Pasted image 20250804152540.png]]

# Day 12
![[Pasted image 20250806144936.png]]


# Day 26

## 서로소 집합 & 상호배타 집합
- 서로 중복 포함된 원소가 없는 집합들
- 집합에 속한 하나의 특정 멤버를 통해 각 집합들을 구분한다.
	- 이를 대표자(representative)라 한다.

- 서로소 집합을 표현하는 방법
	- 연결 리스트
	- 트리
- 서로소 집합 연산
	- `Make-Set( x )`: 집합 생성 (크기가 1인 단위 집합)
	- `Find-Set( x )`: $x$가 속한 집합 찾기 -> 집합 식별자인 대표자 찾기
	- `Union( x, y )`: $x$가 속한 집합 $U$ y가 속한 집합 -> 집합 통합 (합집합)


- 같은 집합의 원소들은 하나의 연결리스트로 관리한다.
- 연결리스트의 맨 앞의 원소를 집합의 대표 원소로 삼는다.
- 각 원소는 집합의 대표 원소를 가리키는 링크를 갖는다.
- ![[Pasted image 20250825094333.png]]

![[Pasted image 20250825094403.png]]
![[Pasted image 20250825094832.png]]
![[Pasted image 20250825094952.png]]
- `Find-Set(c)` $!=$ `Find-Set(d)`
	- -> `Union(c, d)`
		- 예시로 오른쪽 노드를 왼쪽 노드로 합친 것

![[Pasted image 20250825095330.png]]
- 항상 부모 노드 쪽으로 탐색이 일어나고 있음.

### 구현 (수도 코드)
![[Pasted image 20250825101307.png]]

### 구현 (코드)
```java
package test;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

public class DisjointSetTest {
	static int N;
	static int[] parents;
	
	private static void make() {
		for (int i = 0; i < N; i++) {
			parents[i] = i; // make set: 자신을 자신의 부모로 초기화(자신이 곧 루트이자 대표자)
		}
	}
	
	private static int find(int a) { // a가 속한 집합(집합의 대표자) 찾기
		if (parents[a] == a) {
			return a;
		} else {
			return find(parents[a]);
		}
	}
	
	private static boolean union(int a, int b) { // 원소 a, 원소 b가 속한 집합을 합치기
		int aRoot = find(a);
		int bRoot = find(b);
		if (aRoot == bRoot) return false; // 같은 집합이니까 union할 필요 없음
		
		parents[bRoot] = aRoot; // b, a가 아닌, bRoot, aRoot를 사용해야 대표자끼리 연산하는 게 됨.
		return true; // union 성공
	}
	
	public static void main(String[] args) {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		N = 5;
		parents = new int[N];
		
		// 1. make set 처리
		make();
		System.out.println(Arrays.toString(parents));
		System.out.println(union(0, 1));
		System.out.println(Arrays.toString(parents));
		System.out.println(union(2, 1));
		System.out.println(Arrays.toString(parents));
		System.out.println(union(3, 1));
		System.out.println(Arrays.toString(parents));
		System.out.println(union(4, 3));
		System.out.println(Arrays.toString(parents));
		
		System.out.println("===find parent===");
		System.out.println(find(0)); // 4
		System.out.println(find(1)); // 4
		System.out.println(find(2)); // 4
		System.out.println(find(3)); // 4
		System.out.println(find(4)); // 4
				
		System.out.println("===union fail===");
		System.out.println(union(2, 3));
	}

}
```
![[Pasted image 20250825103757.png]]

## 최적화

### Rank를 이용한 Union
- 각 노드는 자신을 루트로 하는 subtree의 높이를 rank로 저장한다.
- 두 집합을 합칠 때 rank가 낮은 집합을 rank가 높은 집합에 붙인다.
![[Pasted image 20250825105051.png]]
- a 노드가 e 노드보다 rank가 높기 때문에 Union 결과에도 rank 변화 없음
![[Pasted image 20250825105104.png]]
- a 노드와 e 노드가 rank가 같다면, a가 부모가 되기 위해서 a의 rank는 증가되어야만 함
### Path compression
- Find-Set을 행하는 과정에서 만나는 모든 노드들이 직접 root를 가리키도록 포인터를 바꾸어 준다.
![[Pasted image 20250825105327.png]]
- 왼쪽과 오른쪽의 트리는 집합의 의미로서는 같다는 성질을 이용한 것.
	- 즉, e의 부모와 h의 부모가 d가 아니고 a여도 상관이 없음.
		- 어차피 결국엔 같은 집합이냐 아니냐, 최상단 루트 부모가 누구냐
		- 이게 해당 로직의 주요 쟁점이기 때문
- 아무튼 `Find-Set(h)`를 실행하는 도중 경로를 압축해주면 됨.
```java
	private static int find(int a) { // a가 속한 집합(집합의 대표자) 찾기
		if (parents[a] == a) {
			return a;
		} else {
			return parents[a] = find(parents[a]);
		}
	}
```

# Day 27

## 최소 신장 트리 (MST)

### 그래프에서 최소 비용과 관련된 문제
- 모든 정점을 연결하는 간선들의 가중치의 합이 최소가 되는 트리 (최소신장트리)
- 두 정점 사이의 최소 비용의 경로 찾기 (최단경로)

![[Pasted image 20250826091941.png]]
- 신장 트리
	- n개의 정점으로 이루어진 무향 그래프에서 n개의 정점과 n-1개의 간선으로 이루어진 트리

- 최소 신장 트리
	- 무향 가중치 그래프에서 신장 트리를 구성하는 간선들의 가중치의 합이 최소인 신장 트리

  
## KRUSKAL 알고리즘
**간선을 하나씩 선택해서 MST를 찾는 알고리즘 (간선 중심, $_E$$C$$_V$$_-$$_1$ 선택 느낌, 그리디로 풀어봄)
1. 최초, 모든 간선을 가중치에 따라서 **오름차순**으로 정렬
2. 가중치가 가장 낮은 **간선**부터 선택하면서 트리를 증가시킴
	- 사이클이 존재하면 남아 있는 간선 중 그 다음으로 가중치가 낮은 간선 선택
3. n - 1 개의 간선이 선택될 때까지 2를 반복

`템플릿 코드드`
```java
package src;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class SWEA_3124 {
	// Union-Find
	public static int[] parents;
	
	public static void make() {
		for (int i = 0; i <= V; i++) {
			parents[i] = -1; // Union By Rank
		}
	}
	
	public static int find(int cur) {
		if (parents[cur] < 0) return cur; // 값이 -1이면 루트 노드를 의미, -2 이하이면 랭크가 증가한 부모 노드를 의미
		return parents[cur] = find(parents[cur]); // 경로 압축
	}
	
	public static boolean union(int a, int b) {
		int aP = find(a);
		int bP = find(b);
		
		// 이미 같은 집합
		if (aP == bP) return false;
		
		// 랭크가 서로 다를 때 (b가 더 큰 랭크) -> 왜 스왑? -> 자식으로 만드는 부분을 하나의 코드로 통일
		if (parents[aP] > parents[bP]) {
			// swap
			int temp = aP;
			aP = bP;
			bP = temp;
		}
		
		// 랭크가 서로 같을 때 -> a의 Rank를 증가 (-1, -2, -3 ... 작아질 수록 랭크가 큼)
		if (parents[aP] == parents[bP]) {
			parents[aP]--;
		}

		// 기본적으로는 b를 a의 자식으로 만듦.
		parents[bP] = aP;
		
		return true; // Union 연산 성공
	}
	
	// Kruskal -> 간선 배열 오름차순 정렬 + Union-Find로 간선 처리	
	public static class Edge implements Comparable<Edge> {
		int from;
		int to;
		int weight;
		
		public Edge(int from, int to, int weight) {
			this.from = from;
			this.to = to;
			this.weight = weight;
		}

		@Override
		public int compareTo(Edge o) {
			return Integer.compare(this.weight, o.weight);
		}
	}
	
	public static Edge[] edges;
	
	// ---
	public static int V;
	public static int E;
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st;
		int T = Integer.parseInt(br.readLine());
		
		for (int test_case = 1; test_case <= T; test_case++) {
			st = new StringTokenizer(br.readLine());
			
			V = Integer.parseInt(st.nextToken());
			E = Integer.parseInt(st.nextToken());
			
			parents = new int[V + 1];
			edges = new Edge[E];
			
			for (int i = 0; i < E; i++) {
				st = new StringTokenizer(br.readLine());
				int from = Integer.parseInt(st.nextToken());
				int to = Integer.parseInt(st.nextToken());
				int weight = Integer.parseInt(st.nextToken());
				edges[i] = new Edge(from, to, weight);
			}
			
			Arrays.sort(edges);
			make();
			
			int cnt = 0;
			long sum = 0;
			for (Edge e : edges) {
				int f = e.from;
				int t = e.to;
				int w = e.weight;
				
				if (!union(f, t)) continue; // union 결과가 !false = true -> 이미 트리 구조에 편입됨 또는 사이클?
				sum += w;
				if (++cnt == V - 1) break;
			}
			
			sb.append("#").append(test_case).append(" ").append(sum).append("\n");
		}
		System.out.print(sb);
	}

}
```

# Day 28

## PRIM 알고리즘

**하나의 정점에서 연결된 간선들 중에 하나씩 선택하면서 MST를 만들어 가는 방식**
1. 임의 정점을 하나 선택해서 시작
2. 선택한 정점과 인접하는 정점들 중의 최소 비용의 간선이 존재하는 정점을 선택
3. 모든 정점이 선택될 때까지 2번 과정을 반복

**서로소인 2개의 집합(2 disjoint-sets) 정보를 유지**
- 트리 정점들(tree vertices) - MST를 만들기 위해 선택된 정점들
- 비트리 정점들(non-tree vertices) - 선택되지 않은 정점들

# Day 31

## 최단경로 1
