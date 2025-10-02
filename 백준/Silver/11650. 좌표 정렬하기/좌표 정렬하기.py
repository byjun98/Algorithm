import sys
input = sys.stdin.readline
N = int(input())
arr = []
for i in range(N):
    x, y = map(int, input().split())
    arr.append((x,y))
ans = sorted(arr, key=lambda a: (a[0],a[1]))
for i in range(len(ans)):
    print(*ans[i])