T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dir = [(0,1), (0,-1), (1,0), (-1,0)]
    max_m = 0
    for i in range(N):
        for j in range(N):
            length = 1
            x, y = i, j
            while True:
                min_val = float('inf')
                next_pos = None
                for dx, dy in dir:
                    ni, nj = x+dy, y+dx
                    if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] < arr[x][y]:
                        if arr[ni][nj] < min_val:
                            min_val = arr[ni][nj]
                            next_pos = (ni,nj)
                if not next_pos:
                    break
                x, y = next_pos
                length += 1
            max_m = max(max_m, length)
    print(f"#{t} {max_m}")