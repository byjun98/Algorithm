A, B = list(map(str, input().split()))
na = int(A[::-1])
nb = int(B[::-1])
print(max(na, nb))