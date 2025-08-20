x = []
y = []
for _ in range(3):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

# x 좌표
if x[0] == x[1]:
    x4 = x[2]
elif x[0] == x[2]:
    x4 = x[1]
else:
    x4 = x[0]

# y 좌표
if y[0] == y[1]:
    y4 = y[2]
elif y[0] == y[2]:
    y4 = y[1]
else:
    y4 = y[0]

print(x4, y4)
