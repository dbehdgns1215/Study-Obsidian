

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


 
