```java
// 선공이면 1,3,5 / 후공이면 2,4,5 순서
int[] myBalls = (order==1) ? new int[]{1,3,5} : new int[]{2,4,5};

for(int b : myBalls){
    if(balls[b][0] == -1) continue; // 이미 치운 공이면 스킵
    targetX = balls[b][0];
    targetY = balls[b][1];

    // 3️⃣ 각 목적구별로 가장 유리한 홀 선택
    for(int[] hole : HOLES){
        // 목적구 -> 홀 단위벡터 계산
        dx = hole[0] - targetX;
        dy = hole[1] - targetY;
        double length = Math.hypot(dx, dy);
        double ux = dx / length;
        double uy = dy / length;

        // 4️⃣ 고스트볼 위치 계산
        double ghostX = targetX - 2*r * ux;
        double ghostY = targetY - 2*r * uy;

        // 5️⃣ 흰 공 → 고스트볼 경로 체크
        boolean blocked = false;
        for(int i=1; i<NUMBER_OF_BALLS; i++){
            if(i == b) continue; // 목표 공 제외
            double cx = balls[i][0];
            double cy = balls[i][1];
            if(cx == -1) continue; // 이미 치운 공 제외

            // 직선 투영 계산
            double t = ((cx - balls[0][0])*(ghostX - balls[0][0]) + 
                        (cy - balls[0][1])*(ghostY - balls[0][1]))
                        / ((ghostX - balls[0][0])*(ghostX - balls[0][0]) + 
                           (ghostY - balls[0][1])*(ghostY - balls[0][1]));
            if(t < 0 || t > 1) continue; // 내 공과 고스트볼 사이 아니면 패스

            // 수직거리
            double closestX = balls[0][0] + t*(ghostX - balls[0][0]);
            double closestY = balls[0][1] + t*(ghostY - balls[0][1]);
            double dist = Math.hypot(cx - closestX, cy - closestY);
            if(dist < 2*r){ blocked = true; break; } // 방해물 있음
        }

        if(blocked) continue; // 장애물 있으면 다음 홀 체크

        // 6️⃣ 각도 + 파워 계산
        double dyShot = ghostY - balls[0][1];
        double dxShot = ghostX - balls[0][0];
        double radian = Math.atan2(dyShot, dxShot);
        double angle = Math.toDegrees(radian);
        if(angle < 0) angle += 360; // 음수 → 0~360

        double distance = Math.hypot(dxShot, dyShot);
        double power = Math.min(distance*1.5, 100); // 단순 거리 기반 파워
        // 7️⃣ 발사 준비 완료
        break; // 성공한 목적구+홀 찾으면 반복 종료
    }
}

```

|기능|함수/연산|설명|
|---|---|---|
|방향 계산|`atan2(dy, dx)`|흰 공 → 고스트볼 방향 각도 계산|
|단위 변환|`toDegrees()`|라디안 → 도|
|음수 처리|`if(angle<0) angle+=360`|0~360도로 각도 통일|
|거리 계산|`Math.hypot(dx, dy)`|피타고라스로 벡터 길이 계산|
|방향만 벡터|`(ux, uy)`|단위 벡터, 방향만 남김|
|고스트볼 위치|`ghostX, ghostY`|목적구 뒤 2r 위치 계산|
|장애물 체크|벡터 내적 t|직선 위에 공이 있으면 skip|
|충돌 거리|`dist < 2*r`|공끼리 닿으면 피함|
|목표 공 선택|for문|여러 목적구 중 치기 쉬운 공 선택|
