import sys
input = sys.stdin.readline

N = int(input())
dancers = {"ChongChong"}

for _ in range(N):
    a, b = input().split()
    if a in dancers or b in dancers:
        dancers.add(a)
        dancers.add(b)

print(len(dancers))
