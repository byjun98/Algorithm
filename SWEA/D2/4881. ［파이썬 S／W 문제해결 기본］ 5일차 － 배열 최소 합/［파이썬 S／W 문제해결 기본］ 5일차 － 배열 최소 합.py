def dfs(n, sm):
    global min_total
    if sm >= min_total:
        return

    if n == N:
        min_total = min(min_total, sm)
        return

    for j in range(N):
        if v[j] == 0:
            v[j] = 1
            dfs(n+1, sm+num[n][j])
            v[j] = 0


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    num = [list(map(int, input().split())) for _ in range(N)]
    v = [0] * N
    min_total = float('inf')
    dfs(0, 0)
    print(f"#{t} {min_total}")