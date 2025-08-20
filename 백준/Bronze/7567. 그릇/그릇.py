# 그릇의 모양을 입력받습니다.
dishes = input()

# 첫 번째 그릇의 높이는 항상 10cm이므로, total_height를 10으로 초기화합니다.
total_height = 10

# 두 번째 그릇부터(인덱스 1) 마지막 그릇까지 반복합니다.
for i in range(1, len(dishes)):
    # 현재 그릇(dishes[i])과 바로 이전 그릇(dishes[i-1])의 모양을 비교합니다.
    
    # 만약 모양이 같다면 (같은 방향으로 포개면)
    if dishes[i] == dishes[i-1]:
        total_height += 5  # 높이를 5 더합니다.
    # 모양이 다르다면 (다른 방향으로 쌓으면)
    else:
        total_height += 10 # 높이를 10 더합니다.

# 최종 계산된 높이를 출력합니다.
print(total_height)