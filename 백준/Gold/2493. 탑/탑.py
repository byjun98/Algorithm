import sys

input = sys.stdin.readline

N = int(input())
heights = list(map(int, input().split()))

stack = []
answer = [0] * N

for i in range(N):
    h = heights[i]

    while stack and stack[-1][1] <= h:
        stack.pop()

    if stack:
        answer[i] = stack[-1][0] + 1

    stack.append((i, h))

print(*answer)
