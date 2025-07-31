# 테스트 케이스 개수 입력
total_case = int(input())

for case_number in range(1, total_case + 1):
    # 격자의 행 개수와 열 개수 입력
    row_count, col_count = map(int, input().split())

    # 격자 입력 받기
    grid = []
    for _ in range(row_count):
        grid.append(list(map(int, input().split())))

    max_total = 0  # 지금까지 찾은 최대 꽃가루 합

    # 모든 칸 하나하나 검사하기
    for row in range(row_count):
        for col in range(col_count):
            power = grid[row][col]  # 이 칸에서 퍼질 수 있는 거리
            total = power           # 먼저 자기 자신 값부터 더하기

            # 위쪽으로 퍼지기
            for step in range(1, power + 1):
                new_row = row - step
                if new_row < 0:
                    break  # 격자 벗어나면 멈춤
                total += grid[new_row][col]

            # 아래쪽으로 퍼지기
            for step in range(1, power + 1):
                new_row = row + step
                if new_row >= row_count:
                    break
                total += grid[new_row][col]

            # 왼쪽으로 퍼지기
            for step in range(1, power + 1):
                new_col = col - step
                if new_col < 0:
                    break
                total += grid[row][new_col]

            # 오른쪽으로 퍼지기
            for step in range(1, power + 1):
                new_col = col + step
                if new_col >= col_count:
                    break
                total += grid[row][new_col]

            # 지금까지 찾은 최대값보다 크면 갱신
            if total > max_total:
                max_total = total

    # 결과 출력
    print(f"#{case_number} {max_total}")
