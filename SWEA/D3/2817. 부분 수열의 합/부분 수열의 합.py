def recur(idx, total):
    global cnt

    if idx == N:
        if total == K:
            cnt += 1
        return

    recur(idx + 1, total + arr[idx])
    recur(idx + 1, total)

T = int(input())
for t in range(1, T + 1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    cnt = 0
    recur(0, 0)

    if K == 0:
        cnt -= 1

    print(f"#{t} {cnt}")
