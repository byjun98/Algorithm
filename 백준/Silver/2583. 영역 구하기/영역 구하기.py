from collections import deque

M, N, K = map(int, input().split())
graph = [[0]*N for _ in range(M)]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for y in range(y1, y2):
        for x in range(x1, x2):
            graph[y][x] = 1

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

def bfs(sy, sx):
    q = deque([(sy, sx)])
    graph[sy][sx] = 1
    area = 1
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < M and 0 <= nx < N and graph[ny][nx] == 0:
                graph[ny][nx] = 1
                q.append((ny, nx))
                area += 1
    return area

areas = []
for y in range(M):
    for x in range(N):
        if graph[y][x] == 0:
            areas.append(bfs(y, x))

areas.sort()
print(len(areas))
print(*areas)
