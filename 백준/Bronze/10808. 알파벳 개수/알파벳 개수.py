c = [0] * 26
arr = list('abcdefghijklmnopqrstuvwxyz')  # ['a','b','c',...,'z']

S = input().strip()

for ch in S:
    if ch in arr:                     # 알파벳만
        idx = arr.index(ch)           # 몇 번째 알파벳인지 찾기
        c[idx] += 1

print(*c)
