import sys
input = sys.stdin.readline
from collections import deque

def bfs(start, arr):
    days = 0
    q = deque(start)

    while q:
        for _ in range(len(q)):
            ci, cj = q.popleft()
            for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                ni, nj = ci + di, cj + dj
                if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 0:
                    arr[ni][nj] = 1
                    q.append((ni, nj))
        if q:
            days += 1

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                return -1
    return days

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
start = []


for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            start.append((i,j))

result = bfs(start, arr)
print(result)