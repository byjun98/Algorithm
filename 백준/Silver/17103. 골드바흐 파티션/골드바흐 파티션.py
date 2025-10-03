import sys
input = sys.stdin.readline

MAX = 1000000
is_prime = [True] * (MAX + 1)
is_prime[0] = is_prime[1] = False

for i in range(2, int(MAX**0.5) + 1):
    if is_prime[i]:
        for j in range(i*i, MAX+1, i):
            is_prime[j] = False

T = int(input())
for _ in range(T):
    N = int(input())
    count = 0
    for p in range(2, N//2 + 1):
        if is_prime[p] and is_prime[N - p]:
            count += 1
    print(count)
