import sys
input = sys.stdin.readline

N, S = map(int, input().split())
arr = list(map(int, input().split()))

count = 0

def dfs(index, current_sum):
    global count

    # 마지막 원소까지 다 본 경우
    if index == N:
        if current_sum == S:
            count += 1
        return

    dfs(index + 1, current_sum + arr[index])

    dfs(index + 1, current_sum)

# 탐색 시작
dfs(0, 0)

# 공집합은 제외해야 함 (합이 0인 공집합도 세지 않음)
if S == 0:
    count -= 1

print(count)
