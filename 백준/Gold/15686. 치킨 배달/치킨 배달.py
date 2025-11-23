import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

house = []
chicken = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            house.append((i, j))
        elif board[i][j] == 2:
            chicken.append((i, j))

min_city_dist = float('inf')
chick_len = len(chicken)

def dfs(start, count, selected):
    global min_city_dist
    if count == M:
        total = 0
        for hr, hc in house:
            dist = float('inf')
            for idx in selected:
                cr, cc = chicken[idx]
                d = abs(hr - cr) + abs(hc - cc)
                if d < dist:
                    dist = d
            total += dist
        if total < min_city_dist:
            min_city_dist = total
        return

    for i in range(start, chick_len):
        selected.append(i)
        dfs(i+1, count+1, selected)
        selected.pop()

dfs(0, 0, [])
print(min_city_dist)
