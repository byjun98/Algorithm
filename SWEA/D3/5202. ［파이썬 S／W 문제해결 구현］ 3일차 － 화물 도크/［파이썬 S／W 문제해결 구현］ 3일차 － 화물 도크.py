T = int(input())
for t in range(1, T + 1):
    N = int(input())
    works = []
    for _ in range(N):
        S, E = map(int, input().split())
        works.append((S, E))
    works.sort(key=lambda x: x[1])

    cnt = 0
    end_time = 0
    for s, e in works:
        if s >= end_time:
            cnt += 1
            end_time = e

    print(f"#{t} {cnt}")
