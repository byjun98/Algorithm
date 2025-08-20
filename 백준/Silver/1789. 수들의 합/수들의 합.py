S = int(input())
cnt = 0
sum_cnt = 0
while sum_cnt <= S:
    cnt += 1
    sum_cnt += cnt

print(cnt - 1)
