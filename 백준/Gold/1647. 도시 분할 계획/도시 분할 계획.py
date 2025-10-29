import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N, M = map(int, input().split())
edges = []

for _ in range(M):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

# 1. 간선을 비용 순으로 정렬
edges.sort()

parent = [i for i in range(N+1)]

total_cost = 0
max_edge = 0  # MST에서 가장 큰 간선

# 2. Kruskal MST
for cost, a, b in edges:
    if find(a) != find(b):  # 사이클 안 만들면 연결
        union(a, b)
        total_cost += cost
        max_edge = cost  # 항상 최신 연결된 간선이 최대 비용 간선 (정렬돼 있으니까)

# 3. 결과 = MST 총 비용 - 가장 큰 간선
print(total_cost - max_edge)
