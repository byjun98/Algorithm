def dfs(stop, cnt, power):
    global min_elc

    if cnt >= min_elc:
        return

    if stop >= N:
        min_elc = min(min_elc, cnt)
        return

    if power > 0:
        dfs(stop + 1 , cnt, power -1)

    if stop < N:
        dfs(stop + 1, cnt + 1, stop_arr[stop - 1] - 1)


T = int(input())
for t in range(1, T + 1):
    arr = list(map(int, input().split()))
    N = arr[0]
    stop_arr = arr[1:]
    min_elc = float('inf')

    dfs(1, 0, stop_arr[0])

    print(f"#{t} {min_elc}")
