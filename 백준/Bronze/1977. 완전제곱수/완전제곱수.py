M = int(input())
N = int(input())
max_sum = 0
max_M = N
v = False
for i in range(int(N**0.5)+1):
    num = i * i
    if M<= num <=N:
        v = True
        max_sum += num
        if num < max_M:
            max_M = num

if v:
    print(max_sum)
    print(max_M)
else: print(-1)