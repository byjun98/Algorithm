import sys
input = sys.stdin.readline

N = int(input())
R = [int(input()) for _ in range(N)]
R.sort()

max_total = 0
for i in range(N):
    weight = R[i] * (N - i)
    if weight > max_total:
        max_total = weight

print(max_total)
