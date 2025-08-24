T = int(input())
for t in range(T):
    n = int(input())
    store = list(map(int, input().split()))
    store.sort()
    sum = 0
    for i in range(len(store)):
        sum += store[i]
    avg = (sum+(n-1)) // n
    print(abs((avg-store[0])*2) + abs((avg-store[n-1])*2))