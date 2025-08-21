T = int(input())
for t in range(1, T + 1):
    N = int(input())
    rc = 0
    rg = 0
    for i in range(N):
        C, G = map(float, input().split())
        rc += C
        rg += G*C
    print(f"{int(rc)} {(rg / rc):.1f}")