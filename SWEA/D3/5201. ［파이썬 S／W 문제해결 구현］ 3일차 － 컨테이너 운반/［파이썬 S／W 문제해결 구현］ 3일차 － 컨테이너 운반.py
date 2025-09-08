T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    w = list(map(int, input().split()))
    k = list(map(int, input().split()))
    total = 0
    k.sort()
    w.sort(reverse=True)
    for i in w:
        for j in range(len(k)):
            if i <= k[j]:
                total += i
                del k[j]
                break
    print(f"#{t} {total}")
