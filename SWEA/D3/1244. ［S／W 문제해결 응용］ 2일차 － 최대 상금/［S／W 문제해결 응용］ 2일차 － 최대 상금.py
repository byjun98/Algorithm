# 카드 교환하기
def shuffle(cnt):
    global max_money
    # 카드를 섞는 경우의 수가 많은데
    # 이때 섞는 회차도 고려 해주어야 한다.
    money = int(''.join(cards))
    if (money, cnt) in check:
        return
    check.add((money,cnt))
    if cnt >= N:   # N번 교환 끝남!
        # 카드의 모양을 확인하고, 상금 계산
        if money > max_money:
            max_money = money
        return
    # 카드 한 번 바꾸는 모든 경우의 수
    # 카드 한 장이랑, 그 카드 뒷 쪽에 있는 카드 한 장이랑 자리 바꾸기
    for i in range(L):
        # i번 카드랑 i번 보다 뒤에있는 카드들 중 한 장 바꾸기
        for j in range(i+1,L):
            # i번이랑 j 번이랑 자리 바꾸기
            cards[i], cards[j] = cards[j], cards[i]
            # 카드를 교환 하는 한 가지 경우의 수가 나왔으면 다음 교환하기
            shuffle(cnt + 1)
            # 다른 경우의 고려할 때는 원래 모양으로 만들어놓고 i번이랑 j 번이랑 바꾸기
            cards[i], cards[j] = cards[j], cards[i]
 
T = int(input())
for tc in range(1,T+1):
    #숫자 카드, 교환횟수
    # cards는 숫자카드 교환을 해야 하니까...list형태로 받고
    # N은 교환 횟수니까 숫자로 받고..
    cards, N = input().split()
    # '321' -> ['3','2','1'], [3, 2, 1]
    cards = list(cards)
    L = len(cards)
    N = int(N)
    check = set()   # 중복 계산 방지를 위한 set
    max_money = 0
    shuffle(0)
    print(f'#{tc} {max_money}')