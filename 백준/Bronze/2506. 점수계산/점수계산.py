N = int(input())
arr = list(map(int, input().split()))

score = 0
num = 0
for i in range(N):
    if arr[i] == 1:
        num += 1      # 연속된 1의 길이
        score += num  # 그 길이만큼 점수 가산
    else:
        num = 0       # 끊기면 초기화

print(score)
