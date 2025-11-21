import sys
input = sys.stdin.readline

INF = 10**12

V, E = map(int, input().split())

dist = [[INF]*(V+1) for _ in range(V+1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    dist[a][b] = c

for k in range(1, V+1):
    for i in range(1, V+1):
        if dist[i][k] == INF:
            continue
        for j in range(1, V+1):
            if dist[k][j] == INF:
                continue
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]
                
answer = INF
for i in range(1, V+1):
    for j in range(1, V+1):
        if i != j:
            if dist[i][j] < INF and dist[j][i] < INF:
                answer = min(answer, dist[i][j] + dist[j][i])

print(answer if answer < INF else -1)
