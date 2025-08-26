arr = input().strip().split(',')
cnt = 0
for i in range(len(arr)):
    if int(arr[i]) is not None:
        cnt += 1
print(cnt)