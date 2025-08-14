T = int(input())
for t in range(1, T + 1):
    N = int(input())
    A = list(map(int, input().split()))
    max_sum = -1  # 단조 증가 수 없으면 -1

    for i in range(N):
        for j in range(i+1, N):  # i < j 조건
            prod = A[i] * A[j]
            s = str(prod)
            ok = True
            for k in range(len(s) - 1):
                if s[k] > s[k+1]:  # 단조 증가 아님
                    ok = False
                    break
            if ok:
                max_sum = max(max_sum, prod)

    print(f"#{t} {max_sum}")
