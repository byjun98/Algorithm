A, B = map(int, input().split())
C = int(input())
n = 60
r = (B+C)//n
A += r
B = (B+C) % n
A %= 24
print(A, B)
