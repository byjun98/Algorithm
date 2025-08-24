T = int(input())
for t in range(T):
    min_n = 100
    n_sum = 0
    num = list(map(int, input().split()))
    for i in range(7):
        if num[i] % 2 == 0:
            n_sum += num[i]
            if num[i] < min_n:
                min_n = num[i]
    print(n_sum, min_n)