N = int(input())
ans = 0
for i in range(N+1):         # i = 0부터 N까지
    for j in range(i, N+1):  # j = i부터 N까지 (i ≤ j 조건)
        ans += i + j         # 도미노 (i,j)의 점수 더하기
print(ans)
