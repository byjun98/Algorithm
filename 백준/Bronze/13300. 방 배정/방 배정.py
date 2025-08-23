N , K = map(int, input().split())
FC = [0] * 7
MC = [0] * 7
cnt = 0
for t in range(N):
    S, Y = map(int, input().split())
    if S == 1: MC[Y] += 1
    elif S == 0: FC[Y] += 1

for i in range(1, 7):
    if FC[i] % K != 0:
        cnt += FC[i]//K + 1
    else: cnt += FC[i]//K
for i in range(1, 7):
    if MC[i] % K != 0:
        cnt += MC[i]//K + 1
    else: cnt += MC[i]//K
print(cnt)
