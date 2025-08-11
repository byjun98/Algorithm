T = 10
for t in range(1, T + 1):
    N = int(input())
    arr = [list(input().strip()) for _ in range(8)]
    cnt = 0
    for i in range(8):
        for j in range(8-N+1):
            for k in range(N//2):
                mirror = True
                if arr[i][j+k] != arr[i][j + N-k-1]:
                    mirror = False
                    break
            if mirror :
                cnt += 1

    for j in range(8):
        for i in range(8-N+1):
            mirror = True
            for k in range(N//2):
                if arr[i+k][j] != arr[i + N - k - 1][j]:
                    mirror = False
                    break
            if mirror:
                cnt += 1

    print(f"#{t} {cnt}")