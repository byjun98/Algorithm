N = int(input())
cnt = 0
for i in range(N):
    group = True
    seen = set()
    prev = ''
    word = list(input())
    for j in word:
        if j != prev:
            if j in seen:
                group = False
                break
            seen.add(j)
        prev = j
    if group:
        cnt += 1
print(cnt)