tall = [int(input()) for _ in range(9)]
total = sum(tall)

found = False
for i in range(9):
    for j in range(i+1, 9):
        # 두 명을 제외했을 때 합이 100이 되면
        if total - tall[i] - tall[j] == 100:
            result = [tall[k] for k in range(9) if k != i and k != j]
            for h in sorted(result):
                print(h)
            found = True
            break
    if found:
        break
