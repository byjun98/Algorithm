import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
t, p = map(int, input().split())
ans = 0

for x in lst:
    ans += (x + t - 1) // t

print(ans)
print(f"{N//p} {N%p}")