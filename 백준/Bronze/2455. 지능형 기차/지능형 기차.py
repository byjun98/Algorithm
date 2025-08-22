max_sum = 0
mx = 0
for i in range(4):
    o1, i1 = map(int, input().split())
    mx += (i1 - o1)
    if mx > max_sum:
        max_sum = mx

print(max_sum)