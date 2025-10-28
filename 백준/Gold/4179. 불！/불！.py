import sys
from collections import deque
input = sys.stdin.readline

R, C = map(int, input().split())
maze = [list(input().strip()) for _ in range(R)]

fire_q = deque()
jihun_q = deque()
fire_time = [[-1]*C for _ in range(R)]  # 불이 도착하는 시간
jihun_time = [[-1]*C for _ in range(R)]  # 지훈이가 도착하는 시간

# 초기 위치 저장
for i in range(R):
    for j in range(C):
        if maze[i][j] == 'F':
            fire_q.append((i, j))
            fire_time[i][j] = 0
        elif maze[i][j] == 'J':
            jihun_q.append((i, j))
            jihun_time[i][j] = 0

# 1. 불의 BFS
while fire_q:
    x, y = fire_q.popleft()
    for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
        nx, ny = x+dx, y+dy
        if 0 <= nx < R and 0 <= ny < C:
            if maze[nx][ny] != '#' and fire_time[nx][ny] == -1:
                fire_time[nx][ny] = fire_time[x][y] + 1
                fire_q.append((nx, ny))

# 2. 지훈이 BFS
while jihun_q:
    x, y = jihun_q.popleft()

    # 탈출 조건 (가장자리에 도달)
    if x == 0 or x == R-1 or y == 0 or y == C-1:
        print(jihun_time[x][y] + 1)
        sys.exit(0)

    for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
        nx, ny = x+dx, y+dy
        if 0 <= nx < R and 0 <= ny < C:
            if maze[nx][ny] == '#' or jihun_time[nx][ny] != -1:
                continue
            # 불이 도달하지 않았거나, 불보다 먼저 도착할 경우만 이동 가능
            if fire_time[nx][ny] == -1 or fire_time[nx][ny] > jihun_time[x][y] + 1:
                jihun_time[nx][ny] = jihun_time[x][y] + 1
                jihun_q.append((nx, ny))

print("IMPOSSIBLE")
