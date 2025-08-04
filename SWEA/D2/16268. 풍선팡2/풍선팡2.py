T = int(input())
    
for t in range(1, T+1):
    N, M = map(int, input().split())
    grid = []
    for row in range(N):
        grid.append(list(map(int, input().split())))
        
    max_sum = 0
    for row in range(N):
        for col in range(M):
            total = grid[row][col]
            if row -1 >= 0:
                total += grid[row - 1][col]
            if row + 1 < N:
                total += grid[row + 1][col]
            if col - 1 >= 0:
                total += grid[row][col - 1]
            if col + 1 < M:
                total += grid[row][col + 1]
                
            if total > max_sum:
                max_sum = total
    print(f"#{t} {max_sum}")