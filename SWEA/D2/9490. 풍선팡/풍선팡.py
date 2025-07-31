T = int(input())
dirs = [(-1,0),(1,0),(0,-1),(0,1)]

for tc in range(1, T+1):
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
    
    max_pollen = 0
    for i in range(N):
        for j in range(M):
            s = grid[i][j]
            # 각 방향으로 1칸부터 grid[i][j]칸까지 폭발
            for dx, dy in dirs:
                for step in range(1, grid[i][j] + 1):
                    ni, nj = i + dx * step, j + dy * step
                    # 범위 안이면 더하고, 벗어나면 그 방향 종료
                    if 0 <= ni < N and 0 <= nj < M:
                        s += grid[ni][nj]
                    else:
                        break
            if s > max_pollen:
                max_pollen = s
    
    print(f"#{tc} {max_pollen}")
