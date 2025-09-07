N, M = map(int, input().split())
num = list(map(int, input().split()))

best = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            total = num[i] + num[j] + num[k]
            if best < total <= M:   # M을 넘지 않으면서 최대값
                best = total

print(best)
