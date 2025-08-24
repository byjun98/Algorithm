max_sum = 0
p = 0
for i in range(1, 6):
    score = map(int, input().split())
    s = sum(score)
    if s > max_sum:
        max_sum = s
        p = i
print(p, max_sum)