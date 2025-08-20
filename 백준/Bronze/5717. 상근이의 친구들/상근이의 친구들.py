while True:
    N, M = map(int, input().split())
    if (N, M) == (0,0):
        break
    else:
        print(N+M)