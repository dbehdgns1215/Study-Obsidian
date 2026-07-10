
# PriorityQueue
- 기본적으로는 오름차순. 즉, 최솟값이 먼저 나오는 최소 힙

```java
class Scoville implements Comparable<Scoville> {
	int scoville;
	public Scoville(int scoville) {
		this.scoville = scoville;
	}
	
	@Override public int compareTo(Scoville o) {
		return Integer.compare(this.scoville, o.scoville);
	}
}
```
- PQ를 사용할 때는 Comparable를 구현해야 함.
	- 안하면 최소힙이지만 구현하면 원하는대로 정렬 가능

