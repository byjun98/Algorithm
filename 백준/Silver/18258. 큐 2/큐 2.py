from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
queue = deque()
result = []

for i in range(T):
    cmd = input().split()
    if cmd[0] == 'push':
        queue.append(int(cmd[1]))
    elif cmd[0] == 'pop':
        if queue:
            result.append(str(queue.popleft()))
        else:
            result.append('-1')
    elif cmd[0] == 'size':
        result.append(str(len(queue)))
    elif cmd[0] == 'empty':
        if queue:
            result.append('0')
        else:
            result.append('1')
    elif cmd[0] == 'front':
        if queue:
            result.append(str(queue[0]))
        else:
            result.append('-1')
    elif cmd[0] == 'back':
        if queue:
            result.append(str(queue[-1]))
        else:
            result.append('-1')

print('\n'.join(result))