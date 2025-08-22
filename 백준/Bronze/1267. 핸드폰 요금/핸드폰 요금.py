N = int(input())
arr = list(map(int, input().split()))
a = 0
b = 0
for i in range(N):
    A = (arr[i]//30+1) * 10
    B = (arr[i]//60+1) * 15
    a += A
    b += B
if a > b:
    print(f"M {b}")
elif b > a:
    print(f"Y {a}")
else:
    print(f"Y M {a}")