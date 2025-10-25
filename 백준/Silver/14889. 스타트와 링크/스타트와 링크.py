N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]

visited = [False] * N
min_diff = float('inf')

def dfs(idx, depth):
    global min_diff

    if depth == N // 2:
        start_team, link_team = [], []
        for i in range(N):
            if visited[i]:
                start_team.append(i)
            else:
                link_team.append(i)

        start_sum = link_sum = 0
        for i in range(N // 2):
            for j in range(i + 1, N // 2):
                a, b = start_team[i], start_team[j]
                start_sum += S[a][b] + S[b][a]
                a, b = link_team[i], link_team[j]
                link_sum += S[a][b] + S[b][a]

        min_diff = min(min_diff, abs(start_sum - link_sum))
        return

    for i in range(idx, N):
        if not visited[i]:
            visited[i] = True
            dfs(i + 1, depth + 1)
            visited[i] = False

dfs(0, 0)
print(min_diff)
