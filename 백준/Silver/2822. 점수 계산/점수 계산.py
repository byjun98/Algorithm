score = []
for t in range(1, 9):
    N = int(input())
    score.append(N)

best = sorted(score, reverse=True)
for i in range(7, 4, -1):
    best.pop(i)

si = []
for i in range(8):
    if score[i] in best:
        si.append(i+1)
print(sum(best))
print(*si)