N = int(input())
space = ' '
star = '*'
for i in range(N,0,-1):
    print(f"{space * (N-i)}{star*i}{star*(i-1)}")
for i in range(2, N + 1):
    print(f"{space * (N-i)}{star*i}{star*(i-1)}")