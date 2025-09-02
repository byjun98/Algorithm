T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # 항상 A를 짧은 쪽으로 두기
    if N > M:
        A, B = B, A
        N, M = M, N

    max_num = -float('inf')

    # A를 B 위에서 슬라이딩
    for i in range(M - N + 1):
        num = 0
        for j in range(N):
            num += A[j] * B[i+j]   # j번째 A와 B[i+j] 곱
        max_num = max(max_num, num)

    print(f"#{t} {max_num}")
