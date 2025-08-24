e = [-1] * 26
arr = input().strip()
for i in range(len(arr)):
    ch = arr[i]
    c = ord(ch) - ord('a')
    if e[c] == -1:
        e[c] = i


print(' '.join(map(str, e)))