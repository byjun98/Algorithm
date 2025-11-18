import sys
input = sys.stdin.readline

n, m = map(int, input().split())

INF = int(1e15)

dist = [[INF] * (n + 1) for _ in range(n + 1)]
next_hop = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    dist[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    dist[a][b] = c
    dist[b][a] = c
    next_hop[a][b] = b
    next_hop[b][a] = a

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]
                next_hop[i][j] = next_hop[i][k]


for i in range(1, n + 1):
    row = []
    for j in range(1, n + 1):
        if i == j:
            row.append('-')
        else:
            row.append(str(next_hop[i][j]))
    print(' '.join(row))
