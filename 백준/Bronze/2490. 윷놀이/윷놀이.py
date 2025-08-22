for i in range(3):
    arr = list(map(int, input().split()))
    z_cnt = 0
    for j in range(4):
        if arr[j] == 0:
            z_cnt += 1
    if z_cnt == 1:
        print('A')
    elif z_cnt == 2:
        print('B')
    elif z_cnt == 3:
        print('C')
    elif z_cnt == 4:
        print('D')
    else : print('E')