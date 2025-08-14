from collections import deque

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, list(input().strip()))) for _ in range(N)]

    # 출발점 찾기
    start = None
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                start = (i, j)
                break
        if start:
            break

    # BFS 탐색
    q = deque([start])
    visited = [[False] * N for _ in range(N)]
    visited[start[0]][start[1]] = True
    found = 0

    # 상하좌우 방향
    directions = [(-1,0), (1,0), (0,-1), (0,1)]

    while q:
        x, y = q.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if maze[nx][ny] == 0:  # 통로면 계속 탐색
                    visited[nx][ny] = True
                    q.append((nx, ny))
                elif maze[nx][ny] == 3:  # 도착점 발견
                    found = 1
                    q.clear()  # 탐색 종료
                    break

    print(f"#{t} {found}")
