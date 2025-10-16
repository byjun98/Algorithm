import sys
input = sys.stdin.readline

while True:
    cnt = 0
    N = int(input())
    if N == 0:
        break
    is_prime = [True] * (2*N + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int((2*N)**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, 2*N+1, i):
                is_prime[j] = False
    for i in range(N+1, 2*N + 1):
        if is_prime[i]:
            cnt += 1
    print(cnt)