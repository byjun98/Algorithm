import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

# 누적합 배열 만들기 (길이 N+1, 0번째는 0으로 초기화)
prefix = [0] * (N + 1)

for i in range(1, N + 1):
    prefix[i] = prefix[i - 1] + arr[i - 1]

# 구간 합 계산
for _ in range(M):
    i, j = map(int, input().split())
    print(prefix[j] - prefix[i - 1])
