import sys
input = sys.stdin.readline

N = int(input())
lst = set(range(1,N+1))
ans = 1
for i in lst:
    ans *= i
print(ans)