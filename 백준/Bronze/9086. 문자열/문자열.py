N = int(input())
for t in range(N):
    arr = input().strip()
    result = []

    result.append(arr[0])
    result.append(arr[-1])
    print(''.join(result))
