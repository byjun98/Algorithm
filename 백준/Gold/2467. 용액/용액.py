import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

left = 0
right = N - 1
min_sum = float('inf')
ans = (0, 0)

while left < right:
    s = arr[left] + arr[right]

    if abs(s) < abs(min_sum):
        min_sum = s
        ans = (arr[left], arr[right])
        if s == 0:
            break

    if s < 0:
        left += 1
    else:
        right -= 1

print(ans[0], ans[1])
