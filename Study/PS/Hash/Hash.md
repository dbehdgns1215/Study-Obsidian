
# HashMap

### getOrDefault(Object key, V defaultValue)
- 키로 한 번만 탐색해서 값이 있으면 그 값을 반환 또는 값이 없으면 지정한 기본값(`0`) 반환.
- `hashMap.put(name, hashMap.getOrDefault(name, 0) + 1)`
	- 해시맵에 `name`이라는 `key`에 `value`를 넣는다... 이때 해시맵에서 `name`으로 `value`를 가져오는데 값(`name`)이 있으면 그 값을 없으면 `0`을 가져오고 그 상태에서 `+ 1`을 한 상태로 `name`에 해당하는 `value`를 넣는 것.
	- 이 느낌적인 느낌을 읽었을 때 이해할 수 있을까?