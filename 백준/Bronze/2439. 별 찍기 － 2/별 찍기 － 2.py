N = int(input())
chr = ' '
star = '*'
for i in range(1, N+1):
    print(chr*(N-i)+star*i)