T = int(input())  # 테스트 케이스 수

for t in range(1, T+1):
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]

    max_sum = 0
    # 모든 시작 위치 탐색
    for i in range(N - M + 1):       # 행
        for j in range(N - M + 1):   # 열
            # MxM 구간 합 구하기
            current_sum = 0
            for x in range(M):
                for y in range(M):
                    current_sum += grid[i + x][j + y]
            # 최대값 갱신
            if current_sum > max_sum:
                max_sum = current_sum

    print(f"#{t} {max_sum}")
