T = int(input())
for t in range(1, T + 1):
    N, S = list(input().strip().split())
    for i in S:
        print(i * int(N), end ='')
    print()