T = int(input())
for t in range(1, T + 1):
    N = int(input())
    result = []
    arr = list(input().split())
    a = arr[:len(arr)//2+len(arr)%2]
    b = arr[(len(arr)+1)//2:]
    for i in range(len(b)):
        result.append(a[i])
        result.append(b[i])

    if len(a) > len(b):
        result.append(a[-1])
    print(f"#{t}", *result)