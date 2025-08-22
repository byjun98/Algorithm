A, B = map(int, input().split())
cnt = 0
arr = []
if A > B:
    for i in range(B+1, A):
        cnt += 1
        arr.append(i)
elif A < B:
    for i in range(A+1, B):
        cnt += 1
        arr.append(i)
arr.sort()
print(cnt)
print(*arr)