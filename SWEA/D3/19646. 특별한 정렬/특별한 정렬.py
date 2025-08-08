T = int(input())
for t in range(1, T + 1):
    N = int(input())
    A = list(map(int, input().split()))
    for i in range(N):
        min_idx = i
        for j in range(i+1, N):
            if A[min_idx] > A[j]:
                min_idx = j
        A[i], A[min_idx] = A[min_idx], A[i]

    result = []

    left = 0
    right = N - 1
    for i in range(10):
        if i % 2 == 1:
            result.append(A[left])
            left += 1
        if i % 2 == 0:
            result.append(A[right])
            right -= 1

    print(f"#{t}", *result)

