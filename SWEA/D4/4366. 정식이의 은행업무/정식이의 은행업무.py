T = int(input())
for t in range(1, T + 1):
    b = input().rstrip()
    tr = input().rstrip()

    b_arr = set()
    for i in range(len(b)):
        if b[i] == '0':
            flip = '1'
        else: flip = '0'
        new_b = b[:i] + flip + b[i+1:]
        b_arr.add(int(new_b, 2))

    tr_arr = set()
    for j in range(len(tr)):
        for k in '012':
            if tr[j] != k:
                new_tr = tr[:j] + k + tr[j+1:]
                tr_arr.add(int(new_tr, 3))
    result = (b_arr & tr_arr).pop()

    print(f"#{t} {result}")
