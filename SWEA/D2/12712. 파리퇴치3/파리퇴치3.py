T = int(input())
for t in range(1, T+1):
    N,M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dir1 = [(0,1),(0,-1),(1,0),(-1,0)]
    dir2 = [(1,1),(-1,1),(-1,-1),(1,-1)]
    max_fly = 0
    for row in range(N):
        for col in range(N):
            fly_sum = arr[row][col]
            for dr, dc in dir1:
                r, c = row, col
                for _ in range(M-1):
                    r += dr
                    c += dc
                    if 0 <= r < N and 0 <= c < N:
                        fly_sum += arr[r][c]
            max_fly = max(max_fly, fly_sum)

    for row in range(N):
        for col in range(N):
            fly_sum = arr[row][col]
            for dr, dc in dir2:
                r, c = row, col
                for _ in range(M-1):
                    r += dr
                    c += dc
                    if 0 <= r < N and 0 <= c < N:
                        fly_sum += arr[r][c]
            max_fly = max(max_fly, fly_sum)    
                    
    print(f"#{t} {max_fly}")

