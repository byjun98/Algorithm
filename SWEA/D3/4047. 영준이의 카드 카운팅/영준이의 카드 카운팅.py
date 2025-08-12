T = int(input())
for t in range(1, T + 1):
    S = input().strip()
    S = [S[i:i+3] for i in range(0, len(S), 3)]
    s_cnt = 13
    d_cnt = 13
    h_cnt = 13
    c_cnt = 13
    Error = 0
    seen = set()

    for i in range(len(S)):
        if S[i] in seen:
            Error = 1
            break
        seen.add(S[i])

        if S[i][0] == 'S':
            s_cnt -= 1
        elif S[i][0] == 'D':
            d_cnt -= 1
        elif S[i][0] == 'H':
            h_cnt -= 1
        else:
            c_cnt -= 1
    if Error:
        print(f"#{t} ERROR")
    else:        
        print(f"#{t} {s_cnt} {d_cnt} {h_cnt} {c_cnt}")

