import sys
input = sys.stdin.readline

board = []
for _ in range(9):
    board.append(list(map(int, input().split())))

# 9행, 9열, 9박스 각각 숫자 존재 여부 표시
row = [[False]*10 for _ in range(9)]
col = [[False]*10 for _ in range(9)]
box = [[False]*10 for _ in range(9)]

# 빈칸 좌표 수집
blanks = []
for i in range(9):
    for j in range(9):
        n = board[i][j]
        if n == 0:
            blanks.append((i, j))
        else:
            row[i][n] = True
            col[j][n] = True
            box[(i//3)*3 + (j//3)][n] = True

found = False

def solve(idx):
    global found
    if found:
        return
    if idx == len(blanks):
        for i in range(9):
            print(*board[i])
        found = True
        return

    x, y = blanks[idx]
    b = (x//3)*3 + (y//3)
    for n in range(1, 10):
        if not row[x][n] and not col[y][n] and not box[b][n]:
            # 숫자 배치
            board[x][y] = n
            row[x][n] = col[y][n] = box[b][n] = True

            solve(idx + 1)
            if found:
                return

            # 되돌리기 (백트래킹)
            board[x][y] = 0
            row[x][n] = col[y][n] = box[b][n] = False

solve(0)
