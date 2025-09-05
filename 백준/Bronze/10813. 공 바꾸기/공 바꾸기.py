N, M = map(int, input().split())
arr = [k for k in range(1, N+1)]
for t in range(1, M+1):
    i , j = map(int, input().split())
    arr[i-1], arr[j-1] = arr[j-1], arr[i-1]
print(*arr)

