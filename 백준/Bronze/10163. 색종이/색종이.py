N = int(input())
arr = [[0]*1001 for _ in range(1001)]
for t in range(1, N+1):
    cnt = 0
    x1, y1, c, r = map(int, input().split())
    x2 = x1 + c
    y2 = y1 + r
    for i in range(y1, y2):
        for j in range(x1 , x2):
            arr[i][j] = t

result = [0] * 1001
for i in range(1001):
    for j in range(1001):
        if arr[i][j] != 0:
            result[arr[i][j]] += 1

for t in range(1, N+1):
    print(result[t])