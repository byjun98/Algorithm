import sys
input = sys.stdin.readline

N, M = map(int, input().split())
seq = []

def dfs(start):
    if len(seq) == M:
        print(*seq)
        return

    for num in range(start, N+1):
        seq.append(num)
        dfs(num)
        seq.pop()

dfs(1)
