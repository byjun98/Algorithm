import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
M = int(input())
C = list(map(int, input().split()))

# 큐(0)인 자료구조의 값만 역순으로 넣기
q = deque([B[i] for i in range(N-1, -1, -1) if A[i] == 0])

for x in C:
    if q:
        print(q.popleft(), end=' ')
        q.append(x)
    else:
        print(x, end=' ')
