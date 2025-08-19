def solve(idx, sum_v):
    global min_v
    if sum_v >= min_v:
        return
    if idx == N:
        if sum_v < min_v:
            min_v = sum_v
        return

    for i in range(N):
        #표시안된거만 사용
        if not check[i]:
            check[i] = 1 #i번째 열을 사용함을 표시
            solve(idx + 1, sum_v + data[idx][i])
            check[i] = 0 # 사용 표시 해제


T = int(input())
for t in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    min_v = 0xffffffff
    check = [0] * N # 중복 열 선택 방지
    solve(0,0)
    print(f"#{t} {min_v}")