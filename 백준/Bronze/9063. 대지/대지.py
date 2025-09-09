N = int(input())
xs = []
ys = []
for _ in range(N):
    x, y = map(int, input().split())
    xs.append(x)
    ys.append(y)

if N == 1:  # 점이 1개면 넓이는 0
    print(0)
else:
    width = max(xs) - min(xs)
    height = max(ys) - min(ys)
    print(width * height)
