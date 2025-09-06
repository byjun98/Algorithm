T = int(input())
arr = [[0]*101 for _ in range(101)]
total = 0
for t in range(T):
    a, b = map(int, input().split())
    for i in range(a, a+10):
        for j in range(b, b+10):
            arr[i][j] = 1
for i in range(101):
    for j in range(101):
        total += arr[i][j]
print(total)
