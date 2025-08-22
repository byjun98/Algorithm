card = [i for i in range(1, 21)]  # 1~20 초기화

for _ in range(10):
    A, B = map(int, input().split())
    # 구간을 역순으로 치환 (인덱스는 0부터 시작하니까 A-1:B)
    card[A-1:B] = reversed(card[A-1:B])

print(*card)
