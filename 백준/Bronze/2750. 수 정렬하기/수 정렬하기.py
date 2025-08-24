T = int(input())
num = []
for t in range(T):
    N = int(input())
    num.append(N)
num.sort()
for i in range (len(num)):
    print(num[i])