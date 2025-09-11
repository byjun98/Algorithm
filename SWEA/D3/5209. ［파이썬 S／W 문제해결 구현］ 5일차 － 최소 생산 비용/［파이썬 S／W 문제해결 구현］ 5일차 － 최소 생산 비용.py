def dfs(row, total):
    global min_cost

    # 가지치기: 현재 비용이 최소보다 크면 중단
    if total >= min_cost:
        return

    # 모든 제품을 다 배정했다면 최소 갱신
    if row == N:
        min_cost = min(min_cost, total)
        return

    # 이번 제품(row)에 대해 모든 공장(col) 시도
    for col in range(N):
        if not used[col]:  # col 공장을 아직 안 썼다면
            used[col] = True
            dfs(row + 1, total + arr[row][col])
            used[col] = False  # 백트래킹


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    used = [False] * N   # 어떤 공장이 이미 선택되었는지
    min_cost = float('inf')

    dfs(0, 0)

    print(f"#{t} {min_cost}")
