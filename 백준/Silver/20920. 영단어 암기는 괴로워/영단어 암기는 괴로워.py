import sys
input = sys.stdin.readline

N, M = map(int, input().split())
ans = {}
lst = [input().strip() for _ in range(N)]
for i in lst:
    if len(i) >= M:
        if i in ans:
            ans[i] += 1
        else:
            ans[i] = 1
    else:
        continue
ans_sort = sorted(ans.items(), key=lambda x:(-x[1], -len(x[0]), x[0]))
for i in range(len(ans_sort)):
    print(ans_sort[i][0])