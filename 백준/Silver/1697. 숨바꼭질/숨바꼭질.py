from collections import deque

def bfs(start, target):
    MAX = 100000
    visited = [0] * (MAX+1)

    q = deque()
    q.append(start)
    visited[start] = 0

    while q:
        x = q.popleft()

        if x == target:
            return visited[x]

        for nx in (x-1, x+1, x*2):
            if 0 <= nx <= MAX and visited[nx] == 0 and nx != start:
                visited[nx] = visited[x] + 1
                q.append(nx)

N, K = map(int, input().split())
print(bfs(N, K))
