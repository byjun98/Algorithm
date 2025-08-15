result = set()
for i in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for r in range(x1, x2):
        for c in range(y1, y2):
            result.add((r,c))

print(len(result))

    