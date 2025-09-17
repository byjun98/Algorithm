from heapq import heappop, heappush
def dijkstra(start, graph, N):
    INF = float('inf')
    dist = [INF] * (N + 1)
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        d, now = heappop(pq)
        if d > dist[now]:
            continue
        for nxt, cost in graph[now]:
            nd = d + cost
            if nd < dist[nxt]:
                dist[nxt] = nd
                heappush(pq, (nd, nxt))
    return dist


T = int(input())
for tc in range(1, T + 1):
    N, M, X = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    reverse_graph = [[] for _ in range(N + 1)]

    for _ in range(M):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))          # 정방향
        reverse_graph[v].append((u, w))  # 역방향

    dist_from_X = dijkstra(X, graph, N)
  
    dist_to_X = dijkstra(X, reverse_graph, N)

    # 왕복 거리 계산
    max_dist = 0
    for i in range(1, N + 1):
        max_dist = max(max_dist, dist_from_X[i] + dist_to_X[i])

    print(f"#{tc} {max_dist}")
