num = [int(input()) for _ in range(10)]
arr = [0] * 101   # 0~100까지 (10의 배수니까 1000까지 커버)
avg = 0

# 카운트 누적
for x in num:
    arr[x // 10] += 1
    avg += x

# 최빈값 찾기
max_n = 0
n = 0
for i in range(101):     # arr 전체 탐색
    if arr[i] > max_n:
        max_n = arr[i]
        n = i

print(avg // 10)   # 평균
print(n * 10)      # 최빈값
