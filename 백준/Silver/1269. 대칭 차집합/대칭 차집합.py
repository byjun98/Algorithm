import sys
input = sys.stdin.readline

N, M = map(int, input().split())
cnt = 0
arr1 = set(map(int, input().split()))
arr2 = set(map(int, input().split()))
cnt += len(arr1-arr2)
cnt += len(arr2-arr1)
print(cnt)