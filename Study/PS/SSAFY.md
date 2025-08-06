

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


