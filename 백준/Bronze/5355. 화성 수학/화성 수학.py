T = int(input())
for t in range(1, T + 1):
    arr = input().split()
    num = float(arr[0])
    for i in range(len(arr)):
        if arr[i] == '@':
            num *= 3
        if arr[i] == '%':
            num += 5
        if arr[i] == '#':
            num -= 7
    print(f"{num:.2f}")