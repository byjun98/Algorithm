N, M = map(int, input().split())
arr = [0]*(N+1)
for t in range(M):
    i, j, k = map(int, input().split())
    for l in range(i, j+1):
        arr[l] = k
print(*arr[1:])