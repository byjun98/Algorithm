import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
vip = [int(input()) for _ in range(M)]

# 피보나치 기반 DP
dp = [0] * (N+1)
dp[0] = 1
dp[1] = 1
for i in range(2, N+1):
    dp[i] = dp[i-1] + dp[i-2]

# 구간별 경우의 수 곱하기
result = 1
prev = 0
for v in vip:
    length = v - prev - 1
    result *= dp[length]
    prev = v
result *= dp[N - prev]

print(result)
