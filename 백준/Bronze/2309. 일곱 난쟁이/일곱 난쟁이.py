tall = [int(input()) for _ in range(9)]
all_tall = sum(tall)
for i in range(8):
    for j in range(i+1, 9):
        if all_tall - (tall[i] + tall[j]) == 100:
            fake1, fake2 = tall[i], tall[j]
            tall.remove(fake1)
            tall.remove(fake2)
            tall.sort()
            for h in tall:
                print(h)
            exit()  # 바로 종료