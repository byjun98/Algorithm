import sys
from collections import deque
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

T = int(input())

for _ in range(T):
    w, h = map(int, input().split())
    board = [list(input().rstrip()) for _ in range(h)]
    
    fire_q = deque()
    person_q = deque()
    
    INF = 10**9
    fire_time = [[INF]*w for _ in range(h)]
    person_time = [[INF]*w for _ in range(h)]
    
    for i in range(h):
        for j in range(w):
            if board[i][j] == '*':
                fire_q.append((i, j))
                fire_time[i][j] = 0
            elif board[i][j] == '@':
                person_q.append((i, j))
                person_time[i][j] = 0
    
    while fire_q:
        x, y = fire_q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < h and 0 <= ny < w:
                if board[nx][ny] != '#' and fire_time[nx][ny] == INF:
                    fire_time[nx][ny] = fire_time[x][y] + 1
                    fire_q.append((nx, ny))
    
    escaped = False
    while person_q and not escaped:
        x, y = person_q.popleft()
        
        if x == 0 or x == h-1 or y == 0 or y == w-1:
            print(person_time[x][y] + 1)
            escaped = True
            break
        
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < h and 0 <= ny < w:
                if board[nx][ny] == '#':
                    continue
                if person_time[nx][ny] != INF:
                    continue
                
                nt = person_time[x][y] + 1
                
                if nt >= fire_time[nx][ny]:
                    continue
                
                person_time[nx][ny] = nt
                person_q.append((nx, ny))
    
    if not escaped:
        print("IMPOSSIBLE")
