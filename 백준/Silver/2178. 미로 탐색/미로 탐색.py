from collections import deque
dirs = [(0,1),(0,-1),(1,0),(-1,0)]

def bfs(si, sj):
    q = deque()
    q.append((si, sj))
    V = [[0] * M for _ in range(N)]
    V[si][sj] = 1

    while q:
        i, j = q.popleft()
        for di, dj in dirs:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 1:
                if V[ni][nj] == 0:
                    V[ni][nj] = V[i][j] + 1
                    q.append((ni,nj))

    return V[N-1][M-1]

N, M = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(N)]
print(bfs(0,0))