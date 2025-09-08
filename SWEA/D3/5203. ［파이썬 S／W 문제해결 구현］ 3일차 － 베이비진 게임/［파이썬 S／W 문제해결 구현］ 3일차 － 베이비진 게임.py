T = int(input())
for t in range(1, T + 1):
    arr = list(map(int, input().split()))
    p1 = arr[::2]
    p2 = arr[1::2]
    cnt1 = [0] * 10
    cnt2 = [0] * 10
    winner = 0

    for i in range(6):
        cnt1[p1[i]] += 1
        if cnt1[p1[i]] >= 3:
            winner = 1
            break
        for j in range(8):
            if cnt1[j] and cnt1[j+1] and cnt1[j+2]:
                winner = 1
                break
        if winner:
            break

        cnt2[p2[i]] += 1
        if cnt2[p2[i]] >= 3:
            winner = 2
            break
        for j in range(8):
            if cnt2[j] and cnt2[j+1] and cnt2[j+2]:
                winner = 2
                break
        if winner:
            break

    print(f"#{t} {winner}")
