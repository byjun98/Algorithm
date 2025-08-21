T = int(input())
for i in range(T):
    N, M = map(int, input().split())
    print(f"You get {N//M} piece(s) and your dad gets {N%M} piece(s).")