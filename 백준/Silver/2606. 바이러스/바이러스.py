def dfs(node):
    visited[node] = True
    for nxt in adj[node]:
        if not visited[nxt]:
            dfs(nxt)

N = int(input())  
V = int(input())
adj = [[] for _ in range(N+1)]
for _ in range(V):
    s, e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)

visited = [False] * (N+1)
dfs(1)

print(visited.count(True) - 1)
