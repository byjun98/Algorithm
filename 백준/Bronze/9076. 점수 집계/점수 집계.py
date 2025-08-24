score = []
N = int(input())
for i in range(N):
    num = list(map(int, input().split()))
    num.sort()
    if max(num[1:4])-min(num[1:4]) >= 4:
        print('KIN')
    else:print(sum(num[1:4]))