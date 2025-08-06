T = 10
for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    max_sum = 0
    row_max = 0    
    for row in range(100):
        row_sum = 0
        for col in range(100):
            row_sum += arr[row][col]
        if row_sum > row_max:
            row_max = row_sum
            
    col_max = 0

    for col in range(100):
        col_sum = 0
        for row in range(100):
            col_sum += arr[row][col]
        if col_sum > col_max:
            col_max = col_sum
    
    
    x_max = 0
    x_sum = 0
    for i in range(100):
        x_sum += arr[i][i]
    x_max = x_sum
    
    y_max = 0
    
    y_sum = 0
    
    for i in range(100):
        y_sum += arr[i][99 - i]
        
    y_max = y_sum
    
    max_sum = max(row_max, col_max, x_max, y_max)
    
    print(f"#{t} {max_sum}")