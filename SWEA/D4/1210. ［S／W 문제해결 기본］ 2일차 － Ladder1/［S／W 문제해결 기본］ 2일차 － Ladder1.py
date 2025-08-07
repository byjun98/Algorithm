T = 10
for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    row = 99
    col = arr[row].index(2)

    while row > 0:
        if col > 0 and arr[row][col - 1] == 1:
            while col > 0 and arr[row][col - 1] == 1:
                col -= 1

        elif col < 99 and arr[row][col + 1] == 1:
            while col < 99 and arr[row][col + 1] == 1:
                col += 1

        row -=1

    print(f"#{t} {col}")

