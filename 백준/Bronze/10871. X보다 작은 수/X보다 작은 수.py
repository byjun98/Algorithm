N, X = map(int, input().split())
arr = list(map(int, input().split()))
ans = []
for i in range(N):
    if X > arr[i]:
        ans.append(arr[i])

print(*ans)