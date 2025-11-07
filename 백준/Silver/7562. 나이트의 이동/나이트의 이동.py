from collections import deque
import sys
input = sys.stdin.readline

def bfs(si,sj,ei,ej):
    q = deque()
    v = [[0]*I for _ in range(I)]
    q.append((si,sj))
    v[si][sj] = 1

    while q:
        ci, cj = q.popleft()
        if ci == ei and cj == ej:
            return v[ci][cj]-1
        for di,dj in ((-2,1),(-1,2),(1,2),(2,1),(-2,-1),(-1,-2),(1,-2),(2,-1)):
            ni, nj = ci+di, cj+dj
            if 0 <= ni < I and 0 <= nj < I and v[ni][nj] == 0:
                v[ni][nj] = v[ci][cj] + 1
                q.append((ni, nj))
    return


T = int(input())
for t in range(1, T+1):
    I = int(input())
    si, sj = map(int, input().split())
    ei, ej = map(int, input().split())
    print(bfs(si,sj,ei,ej))