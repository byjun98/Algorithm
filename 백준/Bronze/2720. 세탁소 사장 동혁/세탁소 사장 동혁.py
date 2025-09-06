T = int(input())
for t in range(T):
    M = [0] * 4
    N = int(input())
    M[0] = N // 25
    M[1] = (N % 25)//10
    M[2] = (N % 25)%10//5
    M[3] = (N % 25)%10%5//1
    print(*M)
