def dfs(c, v):
    global ans
    ans = max(ans, len(v))

    for n in adj[c]:
        if n not in v:
            dfs(n, v + [n])


T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    adj = [[] for _ in range(N+1)]
    for _ in range(M):
        x, y = map(int, input().split())
        adj[x].append(y)
        adj[y].append(x)
    ans = 0

    for s in range(1, N + 1):
        dfs(s, [s])

    print(f"#{t} {ans}")