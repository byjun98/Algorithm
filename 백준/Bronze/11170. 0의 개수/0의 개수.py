T = int(input())
for t in range(T):
    N, M = list(input().strip().split())
    cnt = 0
    for i in range(int(N), int(M)+1):
        for j in str(i):
            if j == '0':
                cnt += 1
    print(cnt)
