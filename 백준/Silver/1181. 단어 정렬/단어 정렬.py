import sys
input = sys.stdin.readline
N = int(input())
arr = []
for i in range(N):
    arr.append(input().strip())
arr = set(arr)
ans = sorted(arr, key=lambda a: (len(a),a))
for i in ans:
    print(f"{i}")