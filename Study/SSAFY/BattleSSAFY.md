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

```java
// BFS 헬퍼 클래스
    private static class BFSNode {
        int row, col;
        Queue<String> actions;
        
        BFSNode(int row, int col, Queue<String> actions) {
            this.row = row;
            this.col = col;
            this.actions = actions;
        }
    }
    
    private static boolean isBlocked(String cell) {
        if (cell == null) return true;
        return cell.equals("R") || cell.equals("W");
    }
    
    private static String tryFireIfAligned(int[] me, int[] target, String[] fireCmds) {
        if (me == null || target == null) return null;

        // 같은 행 (row 동일) → 좌우 발사
        if (me[0] == target[0]) {
            int dist = Math.abs(me[1] - target[1]);
            if (dist > 0 && dist <= 3) {
                // target이 오른쪽이면 R(0), 왼쪽이면 L(2)
                int d = (target[1] > me[1]) ? 0 : 2;
                return fireCmds[d];
            }
        }

        // 같은 열 (col 동일) → 상하 발사
        if (me[1] == target[1]) {
            int dist = Math.abs(me[0] - target[0]);
            if (dist > 0 && dist <= 3) {
                // target이 아래면 D(1), 위면 U(3)
                int d = (target[0] > me[0]) ? 1 : 3;
                return fireCmds[d];
            }
        }

        return null; // 발사 조건 아님
    }
```