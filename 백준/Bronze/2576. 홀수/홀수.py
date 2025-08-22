num = []
for i in range(7):
    N = int(input())
    if N % 2 == 1:
        num.append(N)
if num == []:
    print(-1)
else:
    print(sum(num))
    print(min(num))