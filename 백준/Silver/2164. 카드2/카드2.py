import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
arr = deque(range(1, N+1))
while len(arr) > 1:
    arr.popleft()
    arr.append(arr.popleft())
print(*arr)