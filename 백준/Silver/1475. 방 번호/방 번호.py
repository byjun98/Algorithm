N = input().strip()
arr = [0] * 10
num = list(range(10))
for i in N:
    if i in str(num):
        arr[int(i)] += 1
six = arr[6] + arr[9]
arr[6] = (six +1) // 2
arr[9] = 0

print(max(arr))