import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
cal = list(map(int, input().split()))
max_ans = float('-inf')
min_ans = float('inf')


def dfs(idx, cur, add, sub, mul, div):
    global max_ans, min_ans

    # idx == N이면 모든 숫자 사용 완료
    if idx == N:
        if cur > max_ans:
            max_ans = cur
        if cur < min_ans:
            min_ans = cur
        return

    # 다음 숫자를 가져옴
    next_num = arr[idx]

    # + 사용
    if add > 0:
        dfs(idx + 1, cur + next_num, add - 1, sub, mul, div)

    # - 사용
    if sub > 0:
        dfs(idx + 1, cur - next_num, add, sub - 1, mul, div)

    # * 사용
    if mul > 0:
        dfs(idx + 1, cur * next_num, add, sub, mul - 1, div)

    # / 사용 (음수 나눗셈 주의)
    if div > 0:
        if cur < 0:
            dfs(idx + 1, -(-cur // next_num), add, sub, mul, div - 1)
        else:
            dfs(idx + 1, cur // next_num, add, sub, mul, div - 1)


dfs(1, arr[0], cal[0], cal[1], cal[2], cal[3])

print(max_ans)
print(min_ans)