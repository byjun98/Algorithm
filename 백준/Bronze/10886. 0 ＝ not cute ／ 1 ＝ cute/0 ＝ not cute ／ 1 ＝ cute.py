T = int(input())
n = 0
qcnt = 0
for t in range(T):
    q = int(input())
    if q:
        qcnt += 1
    else:
        n += 1
if qcnt > n:
    print('Junhee is cute!')
else:
    print('Junhee is not cute!')