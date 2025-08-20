A, B, C = map(int, input().split())
if A == B and B == C:
    print(10000 + (A * 1000))
elif A==B and B!=C or A==C and C!=B:
    print(1000 + (A * 100))
elif B==C and C!=A:
    print(1000 + (B * 100))
else:
    print((max(A, B, C) * 100))