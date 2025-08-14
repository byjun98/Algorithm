T = 10
for t in range(1, T + 1):
    N = int(input())
    arr = input().rstrip()
    calc = 0
    for i in range(N):
        if arr[i] == '+':
            continue
        else: calc += int(arr[i])

    print(f"#{t} {calc}")