N, M = map(int, input().split())
X, Y = N, M

# 최대공약수(gcd) 구하기
while M != 0:
    N, M = M, N % M
gcd = N

# 최소공배수(lcm) 구하기
lcm = (X * Y) // gcd

print(gcd)
print(lcm)
