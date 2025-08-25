N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]
cnt = 0
for i in range(N-1, -1, -1):
    if arr[i] <= K:
        cnt += K // arr[i]
        K %= arr[i]
print(cnt)
