import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr1 = set(input().strip() for _ in range(N))
arr2 = list(input().strip() for _ in range(M))
cnt = 0
ans = []
for i in arr2:
    if i in arr1:
        cnt += 1
        ans.append(i)
ans.sort()
print(cnt)
print('\n'.join(ans))
