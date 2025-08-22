arr = []
avg = 0
for i in range(5):
    N = int(input())
    arr.append(N)
    avg += N
arr.sort()
print(int(avg/5))
print(arr[2])