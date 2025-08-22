c = [0] * 10
arr = list('0123456789')

A = int(input())
B = int(input())
C = int(input())

result = str(A * B * C)

for ch in result:
    if ch in arr:
        idx = arr.index(ch)
        c[idx] += 1
for i in range(10):
    print(c[i])


