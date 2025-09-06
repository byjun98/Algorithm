arr = [list(map(int, input().split())) for _ in range(9)]
max_arr = -1
a, b = 0, 0
for i in range(9):
    for j in range(9):
        max_arr = max(arr[i][j], max_arr)
        if arr[i][j] == max_arr:
            a, b = i+1, j+1

print(max_arr)
print(a, b)