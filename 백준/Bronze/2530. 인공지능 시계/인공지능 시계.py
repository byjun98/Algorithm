A, B, C = map(int, input().split())
D = int(input())
t = 60
s = (C+D) % t
m = (B + ((C+D) // t)) % t
h = (A + (B + ((C+D) // t)) // t)
h = h % 24
print(h, m, s)