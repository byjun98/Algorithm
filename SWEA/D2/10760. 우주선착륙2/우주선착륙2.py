T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
    home = 0
    for row in range(N):
        for col in range(M):
            center = grid[row][col]
            cnt = 0
            if row-1 >= 0 and col-1 >= 0 and grid[row-1][col-1] < center:
                cnt += 1
            if row-1 >= 0 and grid[row-1][col] < center:
                cnt += 1
            if row-1 >= 0 and col+1 < M and grid[row-1][col+1] < center:
                cnt += 1
            if col-1 >= 0 and grid[row][col-1] < center:
                cnt += 1
            if col+1 < M and grid[row][col+1] < center:
                cnt += 1
            if row+1 < N and col-1 >= 0 and grid[row+1][col-1] < center:
                cnt += 1
            if row+1 < N and grid[row+1][col] < center:
                cnt += 1
            if row+1 < N and col+1 < M and grid[row+1][col+1] < center:
                cnt += 1
                
            if cnt >= 4:
                home += 1
    print(f"#{t} {home}")
