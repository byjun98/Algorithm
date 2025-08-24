T = int(input())
for t in range(T):
    arr = list(map(int, input().split()))
    arr.sort(reverse = True)
    print(arr[2])