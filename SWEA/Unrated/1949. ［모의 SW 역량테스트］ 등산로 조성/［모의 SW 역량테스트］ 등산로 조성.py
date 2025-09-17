di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def dfs(i, j, length, used):
    global max_len
    max_len = max(max_len, length)  # 최대 길이 갱신

    for d in range(4):
        ni, nj = i + di[d], j + dj[d]
        if not (0 <= ni < N and 0 <= nj < N):
            continue  # 범위 밖이면 무시
        if visited[ni][nj]:
            continue  # 이미 방문했으면 무시

        # 그냥 내려갈 수 있는 경우
        if arr[ni][nj] < arr[i][j]:
            visited[ni][nj] = True
            dfs(ni, nj, length + 1, used)
            visited[ni][nj] = False

        # 공사를 아직 안했고, 깎아서 내려갈 수 있는 경우
        elif not used and arr[ni][nj] - K < arr[i][j]:
            original = arr[ni][nj]            # 원래 높이 저장
            arr[ni][nj] = arr[i][j] - 1      # 현재보다 1만 낮게 깎음
            visited[ni][nj] = True
            dfs(ni, nj, length + 1, True)    # 공사 사용
            visited[ni][nj] = False
            arr[ni][nj] = original           # 원상 복구


T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_height = max(max(row) for row in arr) 

    max_len = 0
    visited = [[False] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == max_height:
                visited[i][j] = True
                dfs(i, j, 1, False)
                visited[i][j] = False

    print(f"#{tc} {max_len}")
