import sys
input = sys.stdin.readline
from collections import deque

def bfs(si, sj, sk, ei, ej, ek, arr):
    q = deque()
    v = [[[0]*C for _ in range(R)] for _ in range(L)]
    q.append((si, sj, sk))
    v[si][sj][sk] = 1

    while q:
        ci, cj, ck = q.popleft()
        if arr[ci][cj][ck] == 'E':
            return v[ci][cj][ck] - 1
        for di, dj, dk in ((0,0,1), (0,0,-1),(0,1,0),(0,-1,0),(1,0,0),(-1,0,0)):
            ni, nj, nk = ci+di, cj+dj, ck+dk
            if 0 <= ni < L and 0 <= nj < R and 0 <= nk < C and v[ni][nj][nk] == 0 and (arr[ni][nj][nk] == '.' or arr[ni][nj][nk] == 'E'):
                v[ni][nj][nk] = v[ci][cj][ck] + 1
                q.append((ni,nj,nk))

    return False



while True:
    L, R, C = map(int, input().split())
    if L == 0 and R == 0 and C == 0:
        break
    arr = []
    for _ in range(L):
        floor = [list(input().strip()) for _ in range(R)]
        arr.append(floor)
        input()
    for i in range(L):
        for j in range(R):
            for k in range(C):
                if arr[i][j][k] == 'S':
                    si, sj, sk = i, j, k
                if arr[i][j][k] == 'E':
                    ei, ej, ek = i, j, k
    ans = bfs(si,sj,sk,ei,ej,ek,arr)
    if ans:
        print(f"Escaped in {ans} minute(s).")
    else:
        print('Trapped!')