```java
// 이전 경로 탐색 결과가 존재하지 않을 경우 다시 탐색
            if (actions.isEmpty()) {
            	positions = findPositions(mapData, START_SYMBOL, TARGET_SYMBOL);
                start = positions[0];
                target = positions[1];
                actions = (start != null && target != null) ? bfs(mapData, start, target, WALL_SYMBOL, DIRS, MOVE_CMDS, FIRE_CMDS) : new LinkedList<>();
            }

            // 탱크를 제어할 명령어를 output의 값으로 지정(type: String)
            String output = actions.isEmpty() ? "A" : actions.poll();
```

```java
            // 이전 경로 탐색 결과가 존재하지 않을 경우 다시 탐색
            if (actions.isEmpty()) {
            	positions = findPositions(mapData, START_SYMBOL, TARGET_SYMBOL);
                start = positions[0];
                target = positions[1];
                actions = (start != null && target != null) ? bfs(mapData, start, target, WALL_SYMBOL, DIRS, MOVE_CMDS, FIRE_CMDS) : new LinkedList<>();
            }

            // 탱크를 제어할 명령어를 output의 값으로 지정(type: String)
            // (while 루프 내부) 출력 명령 정하기 직전에 추가
            positions = findPositions(mapData, START_SYMBOL, TARGET_SYMBOL);
            start = positions[0];
            target = positions[1];

            String output;
            String fireNow = tryFireIfAligned(start, target, FIRE_CMDS);
            if (fireNow != null) {
                // 같은 행/열 + 거리 ≤ 3 → 이번 틱은 발사 우선
                output = fireNow;
                actions.clear(); // 이동 계획은 비워서 방황 방지 (선택적이지만 추천)
            } else {
                // 평소대로 이동 실행
                output = actions.isEmpty() ? "A" : actions.poll();
            }
```

