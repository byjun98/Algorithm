T = int(input())
for i in range(T):
    r, e, c = map(int, input().split())
    if e - c < r:
        print('do not advertise')
    elif e - c == r:
        print('does not matter')
    else: 
        print('advertise')