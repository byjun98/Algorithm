T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [0] * 5001
    for _ in range(N):
        A, B = map(int, input().split())
        for j in range(A, B + 1):
            arr[j] += 1

    P = int(input())
    ans = []
    for _ in range(P):
        C = int(input())
        ans.append(str(arr[C]))

    print(f"#{t} {' '.join(ans)}")
