N, K = map(int, input().split())
arr = list(map(int, input().split()))

# 첫 K일 합
window = sum(arr[:K])
max_sum = window

# 슬라이딩 윈도우
for i in range(K, N):
    window += arr[i]        # 새로 들어온 날
    window -= arr[i - K]    # 빠진 날
    if window > max_sum:
        max_sum = window

print(max_sum)
