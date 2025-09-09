T = int(input())
for t in range(1, T + 1):
    N = int(input())
    c = [0] * 201

    for i in range(N):
        a, b = map(int, input().split())
        a = (a + 1) // 2
        b = (b + 1) // 2
        if a > b:
            a, b = b, a
        for j in range(a, b+1):
            c[j] += 1

    ans = max(c)
    print(f"#{t} {ans}")
