T = int(input())
max_money = 0
for t in range(1, T + 1):
    money = 0
    A, B, C = map(int, input().split())
    if A == B and B == C:
        money = 10000 + (A * 1000)
    elif A == B and B != C or A == C and C != B:
        money = 1000 + (A * 100)
    elif B == C and C != A:
        money = 1000 + (B * 100)
    else:
        money = (max(A, B, C) * 100)
    if money > max_money:
        max_money = money
print(max_money)