
# PriorityQueue
- 기본적으로는 **오름차순**. 즉, **최솟값이 먼저 나오는 최소 힙**

```java
class Scoville implements Comparable<Scoville> {
	int scoville;
	public Scoville(int scoville) {
		this.scoville = scoville;
	}
	
	@Override public int compareTo(Scoville o) {
		return Integer.compare(this.scoville, o.scoville);
		// 오름차순
	}
}
```
- PQ를 사용할 때는 Comparable를 구현해야 함.
	- 안하면 최소힙이지만 구현하면 원하는대로 정렬 가능
- 참고로 내림차순은 `this.scoville`, `o.scoville` 순서를 바꾸던가 아니면 아래처럼
```java
  PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
```
- `Collections`를 활용하면 됨

### `offer()` - 삽입
### `poll()` - 우선순위 가장 높은 값 꺼내기
### `peek()` - 우선순위 가장 높은 값 확인

### `size()` - 큐 크기
### `isEmpty()` - 비어 있는지 확인

