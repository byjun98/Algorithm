N = int(input())
arr = [int(x, 16) for x in input().split()]  # ← 16진수로 읽기

res = []
space = ord(' ')   # 32
dot = ord('.')     # 46
zero = ord('0')    # 48
nine = ord('9')    # 57

for c in arr:
    is_space_or_dot = False
    for k in range(zero, nine + 1):  # '0' ~ '9'
        p = c ^ k
        if p == space or p == dot:
            is_space_or_dot = True
            break
    if is_space_or_dot:
        res.append('.')
    else:
        res.append('-')

print(''.join(res))
