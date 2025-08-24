arr = []
for i in range(10):
    N = int(input())
    arr.append(N%42)
arr = set(arr)
print(len(arr))