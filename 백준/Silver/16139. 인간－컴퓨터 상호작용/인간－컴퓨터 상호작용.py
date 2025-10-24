import sys
input = sys.stdin.readline

S = input().strip()
q = int(input())

prefix = [[0] * 26 for _ in range(len(S) + 1)]

for i, ch in enumerate(S, 1):
    for k in range(26):
        prefix[i][k] = prefix[i - 1][k]
    prefix[i][ord(ch) - 97] += 1

out = []
for _ in range(q):
    a, l, r = input().split()
    l, r = int(l), int(r)
    idx = ord(a) - 97
    out.append(str(prefix[r + 1][idx] - prefix[l][idx]))

print('\n'.join(out))
