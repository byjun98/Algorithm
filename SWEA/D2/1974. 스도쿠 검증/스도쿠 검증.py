T = int(input())
num = set(range(1, 10))

for t in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    result = 1

    # 행 검사
    for row in arr:
        if set(row) != num:
            result = 0
            break

    # 열 검사
    if result:
        for col in range(9):
            if set(arr[row][col] for row in range(9)) != num:
                result = 0
                break

    # 3x3 박스 검사
    if result:
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                block = []
                for r in range(i, i+3):
                    for c in range(j, j+3):
                        block.append(arr[r][c])
                if set(block) != num:
                    result = 0
                    break

    print(f"#{t} {result}")
