import sys

input = sys.stdin.readline

def dfs(n, lst):
    global ans
    if n == M:
        ans.append(lst)
        return
    for i in range(1, N + 1):
        if V[i]==0:
            V[i] = 1
            dfs(n+1, lst+[i])
            V[i] = 0


N, M = list(map(int, input().split()))
ans = []
V = [0] * (N + 1)
dfs(0, [])
for lst in ans:
    print(*lst)