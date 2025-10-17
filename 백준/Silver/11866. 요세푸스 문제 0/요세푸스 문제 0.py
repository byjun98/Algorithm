import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(range(1, N + 1))
ans = []
idx = 0

while arr:
    idx = (idx + K - 1) % len(arr)  # 원형 인덱스
    ans.append(str(arr.pop(idx)))

print(f"<{', '.join(ans)}>")
