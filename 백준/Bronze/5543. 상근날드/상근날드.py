H = []
D = []
min_price = 2000
for b in range(3):
    P = int(input())
    H.append(P)
for c in range(2):
    K = int(input())
    D.append(K)
price = 0
for i in range(3):
    price = min(H[i]+D[0], H[i]+D[1])
    if price < min_price:
        min_price = price
print(min_price-50)