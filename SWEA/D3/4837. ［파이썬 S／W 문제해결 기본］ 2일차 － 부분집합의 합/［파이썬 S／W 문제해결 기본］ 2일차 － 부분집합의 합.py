T = int(input())
for t in range(1, T + 1):
    N, K = list(map(int, input().split()))
    A = list(range(1, 13))
    cnt = 0   
    for i in range(2 ** 12):
        subset = 0
        count = 0
        for j in range(12):
            if i & (1<<j):
                subset += A[j]
                count += 1
        if K == subset and count == N:
            cnt += 1
    print(f"#{t} {cnt}")