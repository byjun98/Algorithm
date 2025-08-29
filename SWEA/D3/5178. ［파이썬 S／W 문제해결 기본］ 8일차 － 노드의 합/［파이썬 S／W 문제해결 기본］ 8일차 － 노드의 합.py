T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    tree = [0] * (N+1)

    for _ in range(M):
        idx, val = map(int, input().split())
        tree[idx] = val

    for i in range(N, 0, -1):
        left = 2*i
        right = 2*i+1
        if left <= N:
            tree[i] += tree[left]
        if right <= N:
            tree[i] += tree[right]

    print(f"#{tc} {tree[L]}")
