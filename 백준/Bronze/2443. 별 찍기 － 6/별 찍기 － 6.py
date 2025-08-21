N = int(input())
for i in range(N+1):
    spaces = i
    stars = 2*(N-i) - 1
    print(" " * spaces + "*" * stars)
