N = int(input())
arr = list(map(int, input().split()))
M = max(arr)
r = 0
for i in range(N):
    r += arr[i]/M*100

print(r/N)