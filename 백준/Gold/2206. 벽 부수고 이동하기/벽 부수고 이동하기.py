import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    q = deque()
    q.append((0, 0, 0))  # (x, y, 벽 부쉈는지)
    visited[0][0][0] = 1  # 시작점 거리 1

    while q:
        x, y, broken = q.popleft()

        # 도착점 도달
        if x == N-1 and y == M-1:
            return visited[x][y][broken]

        for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < M:
                # 이동 가능한 빈 칸 (벽X)
                if arr[nx][ny] == 0 and visited[nx][ny][broken] == 0:
                    visited[nx][ny][broken] = visited[x][y][broken] + 1
                    q.append((nx, ny, broken))

                # 벽인데 아직 안 부쉈을 경우
                elif arr[nx][ny] == 1 and broken == 0 and visited[nx][ny][1] == 0:
                    visited[nx][ny][1] = visited[x][y][broken] + 1
                    q.append((nx, ny, 1))

    return -1  # 도달 불가


N, M = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(N)]
visited = [[[0]*2 for _ in range(M)] for _ in range(N)]  # 3차원 방문 배열

print(bfs())
