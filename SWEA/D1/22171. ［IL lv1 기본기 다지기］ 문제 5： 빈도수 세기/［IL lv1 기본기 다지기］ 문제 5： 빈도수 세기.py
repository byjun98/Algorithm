N = int(input())
arr = list(map(int, input().split()))
cnt = [0]*(N+1)
for i in range(N):
    cnt[arr[i]] += 1

for i in range(N):
    if cnt[i] != 0:
        print(f"{i} {cnt[i]}")