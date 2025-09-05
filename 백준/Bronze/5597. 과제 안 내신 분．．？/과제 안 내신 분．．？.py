S = list(range(1,31))
for t in range(28):
    N = int(input())
    S.remove(N)
print(min(S))
print(max(S))