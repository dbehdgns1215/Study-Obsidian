

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



```java
// ======================= List =======================
List<Integer> arrayList = new ArrayList<>();
List<Integer> linkedList = new LinkedList<>();

// ======================= Queue =======================
Queue<Integer> linkedQueue = new LinkedList<>();
Queue<Integer> arrayDequeQueue = new ArrayDeque<>();

// ======================= Deque =======================
Deque<Integer> linkedDeque = new LinkedList<>();
Deque<Integer> arrayDeque = new ArrayDeque<>();

// ======================= Stack =======================
Deque<Integer> stack = new ArrayDeque<>(); // 추천 방식
Stack<Integer> legacyStack = new Stack<>(); // 구식 방식 (비추천)

// ======================= Set =======================
Set<Integer> hashSet = new HashSet<>();
Set<Integer> treeSet = new TreeSet<>();             // 자동 정렬
Set<Integer> linkedHashSet = new LinkedHashSet<>(); // 입력 순서 유지

// ======================= Map =======================
Map<String, Integer> hashMap = new HashMap<>();
Map<String, Integer> treeMap = new TreeMap<>();             // Key 기준 자동 정렬
Map<String, Integer> linkedHashMap = new LinkedHashMap<>(); // 입력 순서 유지

// ======================= PriorityQueue =======================
PriorityQueue<Integer> minHeap = new PriorityQueue<>(); // 오름차순
PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder()); // 내림차순

// ======================= 2D 구조, 좌표 처리 =======================
boolean[][] visited = new boolean[100][100];           // 방문 체크 배열 

```