N = int(input())
arr = set(map(int, input().split()))
M = int(input())
arr2 = list(map(int, input().split()))

for x in arr2:
    print(1 if x in arr else 0, end=' ')
