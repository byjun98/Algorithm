import sys
from collections import deque
input = sys.stdin.readline

def bfs(start, arr):
    days = 0
    q = deque(start)

    while q:
        for _ in range(len(q)):
            ch, ci, cj = q.popleft()  # 층, 행, 열
            for dh, di, dj in ((0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)):
                nh, ni, nj = ch + dh, ci + di, cj + dj
                if 0 <= nh < H and 0 <= ni < N and 0 <= nj < M and arr[nh][ni][nj] == 0:
                    arr[nh][ni][nj] = 1
                    q.append((nh, ni, nj))
        if q:
            days += 1

    # 모든 토마토 익었는지 확인
    for h in range(H):
        for i in range(N):
            for j in range(M):
                if arr[h][i][j] == 0:
                    return -1
    return days


M, N, H = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

start = []
for h in range(H):
    for i in range(N):
        for j in range(M):
            if arr[h][i][j] == 1:
                start.append((h, i, j))

result = bfs(start, arr)
print(result)
