T = int(input())
for t in range(1, T + 1):
    sum = 0
    N = int(input())
    num = list(map(int, input().split()))
    for i in range(N):
        sum += num[i]

    print(sum)