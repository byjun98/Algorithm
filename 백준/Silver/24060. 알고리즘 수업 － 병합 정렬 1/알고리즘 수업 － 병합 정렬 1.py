import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))
tmp = [0] * N

count = 0
answer = -1

def merge_sort(p, r):
    global count, answer
    if p < r:
        q = (p + r) // 2
        merge_sort(p, q)
        merge_sort(q + 1, r)
        merge(p, q, r)

def merge(p, q, r):
    global count, answer
    i = p
    j = q + 1
    t = p 

    while i <= q and j <= r:
        if A[i] <= A[j]:
            tmp[t] = A[i]
            i += 1
        else:
            tmp[t] = A[j]
            j += 1
        t += 1

    while i <= q:
        tmp[t] = A[i]
        i += 1
        t += 1

    while j <= r:
        tmp[t] = A[j]
        j += 1
        t += 1

    for i in range(p, r + 1):
        A[i] = tmp[i]
        count += 1
        if count == K:
            answer = A[i]

merge_sort(0, N - 1)

print(answer)
