N, M = map(int, input().split())
arr = list(map(int, input().split()))
for t in range(M):
    a_sum = 0
    i, j = map(int, input().split())
    for k in range(i-1, j):
        a_sum += arr[k]
    print(a_sum)
