num = []
max_n = 0
idx = 0
for i in range(9):
    N = int(input())
    num.append(N)
    if num[i] > max_n:
        max_n = num[i]
        idx = i+1

print(max(num))
print(idx)