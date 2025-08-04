T = int(input())

for t in range(1, T + 1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]
    max_total = 0
    
    for row in range(N):
        for col in range(N):
            total = 0
            for i in range(row, -1, -1):
                total += grid[i][col]
            for j in range(col-1, -1, -1):
                total += grid[row][j]
            for k in range(row + 1, N):
                total += grid[k][col]
            for l in range(col + 1, N):
                total += grid[row][l]
                
            if total > max_total:
                max_total = total
                
    print(f"#{t} {max_total}")
