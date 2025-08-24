T = int(input())
for i in range(T):
    N, S = input().split()
    N = int(N)-1
    arr = list(S)
    arr.pop(N)
    S = ''.join(arr)
    print(S)