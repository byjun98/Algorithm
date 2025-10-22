import sys
from collections import deque
input = sys.stdin.readline

# BFS 함수
def bfs(si, sj, graph, visited):
    q = deque()
    q.append((si, sj))
    visited[si][sj] = True
    color = graph[si][sj]

    while q:
        ci, cj = q.popleft()
        for di, dj in ((0,1),(1,0),(0,-1),(-1,0)):
            ni, nj = ci+di, cj+dj
            if 0 <= ni < N and 0 <= nj < N:
                if not visited[ni][nj] and graph[ni][nj] == color:
                    visited[ni][nj] = True
                    q.append((ni, nj))

N = int(input())
arr = [list(input().strip()) for _ in range(N)]

# 색약용 배열 만들기 (R과 G를 같은 색으로 취급)
arr_rg = [[c if c != 'G' else 'R' for c in row] for row in arr]

# 방문 배열
visited1 = [[False]*N for _ in range(N)]  # 일반인
visited2 = [[False]*N for _ in range(N)]  # 색약

normal_cnt = 0
blind_cnt = 0

# 일반인 기준 BFS
for i in range(N):
    for j in range(N):
        if not visited1[i][j]:
            bfs(i, j, arr, visited1)
            normal_cnt += 1

# 색약 기준 BFS
for i in range(N):
    for j in range(N):
        if not visited2[i][j]:
            bfs(i, j, arr_rg, visited2)
            blind_cnt += 1

print(normal_cnt, blind_cnt)
