from collections import deque

N = int(input().strip())

# 이전 수 저장용 (경로 복원)
prev = [0] * (N + 1)
# 방문 여부
visited = [False] * (N + 1)

# BFS 초기화
queue = deque([N])
visited[N] = True

while queue:
    x = queue.popleft()

    # 목표: 1 도달 시 탐색 종료
    if x == 1:
        break

    # 세 가지 연산 순서대로 시도
    for nx in (x - 1, x // 2 if x % 2 == 0 else 0, x // 3 if x % 3 == 0 else 0):
        if nx >= 1 and not visited[nx]:
            visited[nx] = True
            prev[nx] = x  # nx는 x에서 왔음
            queue.append(nx)

# 경로 복원 (1 → ... → N)
path = []
cur = 1
while cur != 0:
    path.append(cur)
    cur = prev[cur]
path.reverse()

# 결과 출력
print(len(path) - 1)
print(*path)
