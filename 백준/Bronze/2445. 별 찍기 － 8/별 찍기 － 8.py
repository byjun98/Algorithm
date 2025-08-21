N = int(input())
space = ' '
star = '*'
for i in range(1, N+1):
    print(f"{star*i}{space * (N-i)}{space * (N-i)}{star*i}")
for j in range(N-1, 0, -1):
    print(f"{star*j}{space * (N-j)}{space * (N-j)}{star*j}")
