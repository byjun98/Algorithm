N = int(input())
arr = list(map(int, input().split()))
X = int(input())

s = set(arr)
cnt = 0
for i in arr:
    target = X - i
    if target in s:
        cnt += 1
print(cnt//2)
