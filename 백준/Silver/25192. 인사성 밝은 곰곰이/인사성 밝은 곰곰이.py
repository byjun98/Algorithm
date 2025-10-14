import sys
input = sys.stdin.readline

N = int(input())
cnt = 0
ans = set()
arr = [input().strip() for _ in range(N)]
for i in range(len(arr)):
    if arr[i] == 'ENTER':
        cnt += len(ans)
        ans.clear()
    else:
        ans.add(arr[i])
cnt += len(ans)
print(cnt)
