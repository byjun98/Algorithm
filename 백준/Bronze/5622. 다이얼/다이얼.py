al = list(input())
sum = 0
for i in range(len(al)):
    if al[i] in 'ABC':
        sum += 3
    elif al[i] in 'DEF':
        sum += 4
    elif al[i] in 'GHI':
        sum += 5
    elif al[i] in 'JKL':
        sum += 6
    elif al[i] in 'MNO':
        sum += 7
    elif al[i] in 'PQRS':
        sum += 8
    elif al[i] in 'TUV':
        sum += 9
    elif al[i] in 'WXYZ':
        sum += 10
    else:
        sum += 2
print(sum)
