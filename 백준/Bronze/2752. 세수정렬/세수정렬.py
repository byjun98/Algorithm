num = list(map(int, input().split()))

for _ in range(2):          # 전체 길이-1번 반복
    for i in range(1, 3):   # 인접한 두 수 비교
        if num[i] < num[i-1]:
            num[i-1], num[i] = num[i], num[i-1]

print(*num)
