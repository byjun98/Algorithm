def pre_order(T):
    global cnt
    if T > 0:
        cnt += 1
        pre_order(left[T]) #visited(T)
        pre_order(right[T]) #pre_order(T.left)
T= int(input())
for t in range(1, T+1):

    E, N = map(int, input().split())
    arr = list(map(int, input().split()))
    V = E + 1
    left = [0] * (V + 1)
    right = [0] * (V + 1)

    for i in range(E):

        p, c = arr[i*2], arr[i*2+1]
    # for i in range(0, E*2, 2):
    #     p, c = arr[i], arr[i+1]
        if left[p] == 0:    # 왼쪽자식이 아직 없으면
            left[p] = c
        else:               # 왼쪽자식이 있는 경우
            right[p] = c
    cnt = 0
    pre_order(N)
    print(f"#{t} {cnt}")