T = int(input())
for t in range(1, T+1):
    N = int(input())
    prices = list(map(int, input().split()))

    total = 0
    max_price = 0

    for i in range(N-1, -1, -1):
        if prices[i] > max_price:
            max_price = prices[i]
        else:
            total += max_price - prices[i]

    print(f"#{t} {total}")
