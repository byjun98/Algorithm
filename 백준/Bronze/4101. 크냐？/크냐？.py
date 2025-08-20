A, B = 1, 1
while A > 0:
    A, B = map(int, input().split())
    if A > B:
        print('Yes')
    elif A == 0:
        break
    else:
        print('No')