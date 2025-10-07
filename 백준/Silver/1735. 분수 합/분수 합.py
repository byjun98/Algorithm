import sys
input = sys.stdin.readline

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

A1, A2 = map(int, input().split())
B1, B2 = map(int, input().split())

C1 = (B2*A1) + (A2*B1)
C2 = A2 * B2

common_divisor = gcd(C1, C2)

final_C1 = C1 // common_divisor
final_C2 = C2 // common_divisor

print(f"{final_C1} {final_C2}")