import sys
input = sys.stdin.readline
from collections import deque


N, K = map(int, input().split())
max = 100001
dist = [-1] * max
dist[N] = 0

q = deque([N])

while q:
    x = q.popleft()

    if x == K:
        print(dist[x])
        break

    if 0 <= 2*x < max and dist[2*x] == -1:
        dist[2*x] = dist[x]
        q.appendleft(2*x)

    for nx in (x-1, x+1):
        if 0<=nx < max and dist[nx] == -1:
            dist[nx] = dist[x] + 1
            q.append(nx)
