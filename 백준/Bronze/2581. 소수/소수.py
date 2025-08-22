N = int(input())
M = int(input())
arr = []
num_sum = 0
for i in range(N, M+1):
    if i < 2:
        continue
    num = True
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            num = False
            break
    if num:
        arr.append(i)
        num_sum += i

if arr == []:
    print(-1)
else:
    print(num_sum)
    print(min(arr))