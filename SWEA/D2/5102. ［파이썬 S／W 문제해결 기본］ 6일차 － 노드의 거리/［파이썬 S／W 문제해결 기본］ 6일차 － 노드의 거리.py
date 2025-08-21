from collections import deque

def bfs(S, G, V, adj):
    visited = [0] * (V+1)
    q = deque([S])
    visited[S] = 1

    while q:
        cur = q.popleft()
        if cur == G:
            return visited[cur] - 1
        for nxt in adj[cur]:
            if visited[nxt] == 0:
                q.append(nxt)
                visited[nxt] = visited[cur] + 1
    return 0

T = int(input())
for t in range(1, T+1):
    V, E = map(int, input().split())
    adj = [[] for _ in range(V+1)]

    for _ in range(E):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)

    S, G = map(int, input().split())
    ans = bfs(S, G, V, adj)
    print(f"#{t} {ans}")
