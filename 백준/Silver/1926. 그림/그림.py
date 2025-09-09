from collections import deque

n, m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]

# 4방향 델타 (상, 하, 좌, 우)
di, dj = [-1,1,0,0], [0,0,-1,1]

visited = [[0]*m for _ in range(n)]

def bfs(si, sj):
    q = deque([(si, sj)])
    visited[si][sj] = 1
    area = 1  # 시작칸 포함 넓이

    while q:
        ci, cj = q.popleft()
        for d in range(4):
            ni, nj = ci + di[d], cj + dj[d]
            if 0 <= ni < n and 0 <= nj < m:
                if paper[ni][nj] == 1 and not visited[ni][nj]:
                    visited[ni][nj] = 1
                    q.append((ni, nj))
                    area += 1
    return area

cnt = 0          # 그림 개수
max_area = 0     # 가장 넓은 그림의 넓이

for i in range(n):
    for j in range(m):
        if paper[i][j] == 1 and not visited[i][j]:
            cnt += 1
            max_area = max(max_area, bfs(i, j))

print(cnt)
print(max_area)
