a, b, c = map(int, input().split())
m = max(a, b, c)
sm = 0
total = a + b + c - m
while total <= m:
    m -= 1
print(a+b+c+m-max(a,b,c))