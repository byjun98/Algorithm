A = []
B = []
for i in range(10):
    N = int(input())
    A.append(N)
for i in range(10):
    M = int(input())
    B.append(M)
A.sort(reverse=True)
B.sort(reverse=True)
print(sum(A[:3]), sum(B[:3]))