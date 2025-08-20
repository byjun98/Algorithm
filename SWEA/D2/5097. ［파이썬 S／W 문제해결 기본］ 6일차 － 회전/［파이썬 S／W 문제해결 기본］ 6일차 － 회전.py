T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    num = list(map(int, input().split()))
    r = M % N
    print(f"#{t} {num[r]}")