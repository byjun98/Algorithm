T = int(input())
for t in range(T):
    s = int(input())
    n = int(input())
    sum = s
    for i in range(n):
        q, p = map(int, input().split())
        sum += (q * p)
    print(sum)