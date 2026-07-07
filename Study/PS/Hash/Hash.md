
# HashMap

### 선언
> `hashMap<String, Integer> hm = new HashMap<>();`

### 추가/수정
- `put(keym value)` - 무조건 덮어씀
- `putIfAbsent(key, value)` - 이미 값 있으면 덮어쓰지 않음

### 조회
- `get(key)`
- `getOrDefault(key, default)` - key가 있으면 value, 없으면 기본값 반환

### 삭제
- `remove(key)`
- `clear()` - 전체 삭제

### 검사
- `containsKey(key)` - 특정 key에 대한 Value 확인. ($O(1)$)
- `containsValue(value)` - 특정 Value가 존재하는지 확인. ($O(N)$)

### 기타
- `size()` - k-v 쌍 개수
- `isEmpty()` - `size() == 0`과 동일한 상황이니?

### getOrDefault(Object key, V defaultValue)
- 키로 한 번만 탐색해서 값이 있으면 그 값을 반환 또는 값이 없으면 지정한 기본값(`0`) 반환.
- `hashMap.put(name, hashMap.getOrDefault(name, 0) + 1)`
	- 해시맵에 `name`이라는 `key`에 `value`를 넣는다... 이때 해시맵에서 `name`으로 `value`를 가져오는데 값(`name`)이 있으면 그 값을 없으면 `0`을 가져오고 그 상태에서 `+ 1`을 한 상태로 `name`에 해당하는 `value`를 넣는 것.
	- 이 느낌적인 느낌을 읽었을 때 이해할 수 있을까?


### 순회 패턴

#### Key와 Value 모두 필요할 때
```java
for (Map.Entry<String, Integer> entry : map.entrySet()) {
    String key = entry.getKey();
    Integer value = entry.getValue();
}
```
- `EntrySet` 순회.
	- `keySet()`으로 Key 찾고 `get()`으로 Value를 또 찾는 오버헤드를 줄임.

#### Key만 필요할 때
```java
for (String key : map.keySet()) {
    // 순수하게 Key 리스트만 뽑을 때 사용
}
```
- `KeySet` 순회.
	- 키 모아서 `Set`으로 반환

#### Value만 필요할 때
```java
for (Integer value : map.values()) {
	// 순수하게 Value 리스트만 뽑을 때 사용
}
```
- `values` 순회
	- 밸류 모아서 `Collection`으로 반환

