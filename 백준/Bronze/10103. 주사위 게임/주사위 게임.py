T = int(input())
A = 100
B = 100
for t in range(T):
    N, M = map(int, input().split())
    if N == M:
        continue
    if N > M:
        B -= N
    elif N < M:
        A -= M
print(A)
print(B)