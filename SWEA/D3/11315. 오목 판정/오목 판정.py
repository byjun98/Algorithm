T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(input().strip()) for _ in range(N)]
    dir = [(0,1), (1,0), (1,1), (1,-1)]
    max_sum=0
    omok = False
    for row in range(N):
        for col in range(N):
            for dr, dc in dir:
                cnt = 0
                r, c = row, col
                for _ in range(5):
                        if 0 <= r < N and 0 <= c < N and arr[r][c] == 'o':
                            cnt += 1
                            if cnt == 5:
                                omok = True
                                break
                        r += dr
                        c += dc
    
    if omok is True:
        print(f"#{t} YES")
    
    else:
         print(f"#{t} NO")                   
                        
                    
