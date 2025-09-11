def dfs(worker, prob):
    global max_prob

    if prob <= max_prob:
        return

    if worker == N:
        max_prob = max(max_prob, prob)
        return

    for task in range(N):
        if not used[task]:
            used[task] = True
            dfs(worker + 1, prob * arr[worker][task] / 100)
            used[task] = False


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    used = [False] * N
    max_prob = 0.0

    dfs(0, 1.0)

    print(f"#{t} {max_prob*100:.6f}")
