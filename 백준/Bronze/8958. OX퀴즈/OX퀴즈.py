# 테스트 케이스의 개수를 입력받습니다.
T = int(input())

for t in range(T):
    arr = input().strip()
    
    # 각 테스트 케이스마다 총점과 연속 점수를 0으로 초기화해야 합니다.
    total_score = 0
    consecutive_score = 0
    
    # 문자열의 각 문자를 확인합니다.
    for char in arr:
        # 만약 문자가 'O'라면
        if char == 'O':
            consecutive_score += 1      # 연속 점수를 1 증가시킵니다.
            total_score += consecutive_score # 증가된 연속 점수를 총점에 더합니다.
        # 만약 문자가 'X'라면
        else:
            consecutive_score = 0       # 연속이 끊겼으므로 연속 점수를 0으로 리셋합니다.
            
    # 해당 테스트 케이스의 최종 점수를 출력합니다.
    print(total_score)