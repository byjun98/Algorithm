T = int(input())
for t in range(1, T+1):
    data = list(map(int, input().split()))
    N = data[0]             # 학생 수
    scores = data[1:]       # 점수들
    
    scores.sort(reverse=True)   # 내림차순 정렬
    
    max_n = scores[0]
    min_n = scores[-1]
    
    # 가장 큰 인접 차이 찾기
    max_gap = 0
    for i in range(N-1):
        gap = scores[i] - scores[i+1]
        if gap > max_gap:
            max_gap = gap
    
    print(f"Class {t}")
    print(f"Max {max_n}, Min {min_n}, Largest gap {max_gap}")
