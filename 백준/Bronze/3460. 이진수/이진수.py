T = int(input())
for i in range(T):
    N = int(input())
    pos = 0
    arr = []
    while N > 0:
        if N % 2 == 1:
            arr.append(pos)
        N //= 2
        pos += 1
    print(*arr)