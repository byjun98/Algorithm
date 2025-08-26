arr = list(input().strip())
cnt = 0
for i in range(len(arr)):
    for j in 'aeiou':
        if arr[i] == j:
            cnt += 1
print(cnt)