arr = [list(input()) for _ in range(5)]
result = []
max_len = max(len(i) for i in arr)

for j in range(max_len):
    for i in range(5):
        if j < len(arr[i]):
            result.append(arr[i][j])

print(''.join(result))