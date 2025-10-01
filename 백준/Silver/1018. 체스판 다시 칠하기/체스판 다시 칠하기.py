N, M = map(int, input().split())
board = [input().strip() for _ in range(N)]

def count_repaints(x, y):
    repaint_w = 0  # 왼쪽 위가 W인 경우
    repaint_b = 0  # 왼쪽 위가 B인 경우
    for i in range(8):
        for j in range(8):
            current = board[x+i][y+j]
            # 체스판 패턴에 따라 기대되는 색깔
            if (i + j) % 2 == 0:  # (짝수 칸)
                if current != 'W':  # W 시작일 때
                    repaint_w += 1
                if current != 'B':  # B 시작일 때
                    repaint_b += 1
            else:  # (홀수 칸)
                if current != 'B':  # W 시작일 때
                    repaint_w += 1
                if current != 'W':  # B 시작일 때
                    repaint_b += 1
    return min(repaint_w, repaint_b)

result = 64  # 최악의 경우 64칸 다 칠해야 함
for i in range(N-7):     # 8×8 시작 행
    for j in range(M-7): # 8×8 시작 열
        result = min(result, count_repaints(i, j))

print(result)
