T = int(input())
for t in range(T):
    cnt = 0
    P, M = map(int, input().split())
    C = [0] * (M+1)
    for i in range(P):
        A = int(input())
        C[A] += 1
        if C[A] > 1:
            cnt += 1
    print(cnt)

