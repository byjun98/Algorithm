H, M = map(int, input().split())

if M < 45:
    M += 60 - 45   # M -= 45 대신 M+15 로 써도 됨
    H -= 1
    if H < 0:
        H = 23
else:
    M -= 45

print(H, M)
