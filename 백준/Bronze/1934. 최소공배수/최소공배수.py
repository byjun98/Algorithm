T = int(input())
for _ in range(T):
    A, B = map(int, input().split())

    # 원래 값 보존 (LCM 계산용)
    x, y = A, B

    # GCD 구하기 (유클리드 호제법)
    while B != 0:
        A, B = B, A % B
    g = A  # 최대공약수

    # 최소공배수 계산
    print(x * y // g)
