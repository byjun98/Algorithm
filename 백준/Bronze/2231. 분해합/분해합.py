N = int(input())
answer = 0

for M in range(1, N):
    total = M + sum(int(d) for d in str(M))
    if total == N:
        answer = M
        break

print(answer)
