from itertools import combinations
from copy import deepcopy
from collections import deque

N, M, D = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dy = [0, -1, 0]
dx = [-1, 0, 1]

def bfs(board, start_col):
    visited = [[False]*M for _ in range(N)]
    q = deque([(N-1, start_col, 1)])
    visited[N-1][start_col] = True

    while q:
        y, x, dist = q.popleft()
        if dist > D:
            break
        if board[y][x] == 1:
            return (y, x)
        for i in range(3):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx]:
                visited[ny][nx] = True
                q.append((ny, nx, dist+1))
    return None

def simulate(archers):
    tmp = deepcopy(board)
    kill = 0

    for _ in range(N):
        targets = set()

        for col in archers:
            target = bfs(tmp, col)
            if target:
                targets.add(target)

        for y, x in targets:
            tmp[y][x] = 0
            kill += 1

        tmp.pop()
        tmp.insert(0, [0]*M)

    return kill

ans = 0
for archers in combinations(range(M), 3):
    ans = max(ans, simulate(archers))

print(ans)
