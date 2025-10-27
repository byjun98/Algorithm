N, M = map(int, input().split())
arr = []

def dfs(start):
    if len(arr) == M:
        print(*arr)
        return
    
    for i in range(start, N + 1):
        arr.append(i)
        dfs(i + 1)
        arr.pop()

dfs(1)
