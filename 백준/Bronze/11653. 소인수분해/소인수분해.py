N = int(input())
while N % 2 == 0:
    print(2)
    N //= 2
for i in range(3, 10000000,2):
    while N % i == 0:
        print(i)
        N //= i