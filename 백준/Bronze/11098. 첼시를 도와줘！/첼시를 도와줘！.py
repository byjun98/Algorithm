T = int(input())
for _ in range(T):
    p = int(input())
    max_price = 0
    best_player = ""
    for _ in range(p):
        price, name = input().split()
        price = int(price)
        if price > max_price:
            max_price = price
            best_player = name
    print(best_player)
