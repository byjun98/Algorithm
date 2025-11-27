import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
B, C = map(int, input().split())

cnt = 0

for Ai in arr:
    cnt += 1
    Ai -= B

    if Ai > 0:
        cnt += (Ai + C - 1) // C

print(cnt)
