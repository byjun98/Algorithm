A = list(input().strip())
B = list(input().strip())
cnt = 0
length = len(A) + len(B)
for i in range(len(A)):
    if A[i] in B:
        cnt += 1
        B.remove(A[i])
print(length - cnt*2)