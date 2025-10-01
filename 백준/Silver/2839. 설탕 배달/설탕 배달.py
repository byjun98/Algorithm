N = int(input())
cnt = 0
ans = 0

while N > 0:
    if N % 5 == 0:
        ans += N//5
        ans += cnt
        break
    cnt += 1
    N -= 3
if ans == 0:
    if N % 3 == 0:
        print(cnt)
    else:
        print(-1)
else:
    print(ans)


