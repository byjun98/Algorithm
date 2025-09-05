N, M = map(int, input().split())
arr = [i for i in range(1, N + 1)]
for t in range(M):
    i, j = map(int, input().split())
    arr[i-1:j] = arr[i-1:j][::-1]
print(*arr)