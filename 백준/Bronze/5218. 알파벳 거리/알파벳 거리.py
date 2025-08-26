N = int(input())
for t in range(N):
    A, B = list(input().strip().split())
    result = []
    for i in range(len(A)):
        num = ord(B[i]) - ord(A[i])
        if num < 0:
            result.append(num%26)
        else: result.append(num)


    print(f"Distances:",*result)