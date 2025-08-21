T = int(input())
sum = 0
for t in range(1, T + 1):
    N, M = map(float, input().split())
    sum += M % N
print(int(sum))
