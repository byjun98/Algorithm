dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def count_bricks(b):
    cnt = 0
    for row in b:
        for v in row:
            if v != 0:
                cnt += 1
    return cnt

def top_brick_row(b, col, H):
    for r in range(H):
        if b[r][col] != 0:
            return r
    return -1

def explode(b, sr, sc, H, W):
    if b[sr][sc] == 0:
        return

    q = [(sr, sc, b[sr][sc])]
    head = 0
    b[sr][sc] = 0

    while head < len(q):
        r, c, power = q[head]
        head += 1

        dist = power - 1
        if dist <= 0:
            continue

        for k in range(4):
            nr, nc = r, c
            for _ in range(dist):
                nr += dr[k]
                nc += dc[k]
                if nr < 0 or nr >= H or nc < 0 or nc >= W:
                    break
                if b[nr][nc] != 0:
                    q.append((nr, nc, b[nr][nc]))
                    b[nr][nc] = 0

def apply_gravity(b, H, W):
    for c in range(W):
        bottom = H - 1
        for r in range(H - 1, -1, -1):
            if b[r][c] != 0:
                val = b[r][c]
                b[r][c] = 0
                b[bottom][c] = val
                bottom -= 1

def dfs(depth, b, N, H, W, best_ref):
    remain = count_bricks(b)
    if remain < best_ref[0]:
        best_ref[0] = remain
    if remain == 0 or depth == N:
        return

    for c in range(W):
        r = top_brick_row(b, c, H)
        if r == -1:
            dfs(depth + 1, b, N, H, W, best_ref)
        else:
            nb = [row[:] for row in b]
            explode(nb, r, c, H, W)
            apply_gravity(nb, H, W)
            dfs(depth + 1, nb, N, H, W, best_ref)

T = int(input().strip())
for tc in range(1, T + 1):
    N, W, H = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(H)]
    best_ref = [10**9]
    dfs(0, board, N, H, W, best_ref)
    print("#{} {}".format(tc, best_ref[0]))
