T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    arr = []
    for _ in range(N):
        arr.append(input().strip())

    # cost[i][0] = 행 i를 W로 칠하는 비용
    # cost[i][1] = 행 i를 B로 칠하는 비용
    # cost[i][2] = 행 i를 R로 칠하는 비용
    cost = [[0]*3 for _ in range(N)]
    for i in range(N):
        cntW = 0
        cntB = 0
        cntR = 0
        for j in range(M):
            if arr[i][j] != 'W':
                cntW += 1
            if arr[i][j] != 'B':
                cntB += 1
            if arr[i][j] != 'R':
                cntR += 1
        cost[i][0] = cntW
        cost[i][1] = cntB
        cost[i][2] = cntR

    ans = N * M

    # i : W 마지막 행
    # j : B 마지막 행
    # R은 j+1부터 끝까지
    for i in range(N - 2):
        for j in range(i + 1, N - 1):
            total = 0
            # W 구간
            for r in range(0, i + 1):
                total += cost[r][0]
            # B 구간
            for r in range(i + 1, j + 1):
                total += cost[r][1]
            # R 구간
            for r in range(j + 1, N):
                total += cost[r][2]

            if total < ans:
                ans = total

    print(f"#{t} {ans}")
