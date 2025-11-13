import heapq
import sys
input = sys.stdin.readline

def dijkstra(start, graph):
    INF = float('inf')
    dist = [INF] * (N + 1)
    dist[start] = 0
    pq = [(0, start)]  # (거리, 노드)

    while pq:
        cost, now = heapq.heappop(pq)
        if dist[now] < cost:
            continue
        for nxt, time in graph[now]:
            new_cost = cost + time
            if new_cost < dist[nxt]:
                dist[nxt] = new_cost
                heapq.heappush(pq, (new_cost, nxt))
    return dist


# 입력
N, M, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]
reverse = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, t = map(int, input().split())
    graph[a].append((b, t))
    reverse[b].append((a, t))  # 방향 반대로 저장

# X에서 다른 마을로 (돌아올 길)
go = dijkstra(X, graph)

# 다른 마을에서 X로 (가는 길)
back = dijkstra(X, reverse)

# 왕복 거리 계산
max_time = 0
for i in range(1, N + 1):
    total = go[i] + back[i]
    if total > max_time:
        max_time = total

print(max_time)
