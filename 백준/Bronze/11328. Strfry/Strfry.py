T = int(input())
for _ in range(T):
    A, B = input().split()
    if sorted(A) == sorted(B):
        print("Possible")
    else:
        print("Impossible")
