T = int(input())
v = input()
acnt = 0
bcnt = 0
for i in range(T):
    if v[i] == 'A':
        acnt += 1
    elif v[i] == 'B':
        bcnt += 1
if acnt > bcnt:
    print('A')
elif acnt < bcnt:
    print('B')
else:
    print('Tie')