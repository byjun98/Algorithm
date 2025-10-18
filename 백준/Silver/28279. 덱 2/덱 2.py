import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
dq = deque()
output = []

for _ in range(n):
    cmd = input().strip().split()

    if cmd[0] == '1':
        dq.appendleft(int(cmd[1]))
    elif cmd[0] == '2':
        dq.append(int(cmd[1]))
    elif cmd[0] == '3':
        output.append(str(dq.popleft()) if dq else '-1')
    elif cmd[0] == '4':
        output.append(str(dq.pop()) if dq else '-1')
    elif cmd[0] == '5':
        output.append(str(len(dq)))
    elif cmd[0] == '6':
        output.append('1' if not dq else '0')
    elif cmd[0] == '7':
        output.append(str(dq[0]) if dq else '-1')
    elif cmd[0] == '8':
        output.append(str(dq[-1]) if dq else '-1')

sys.stdout.write('\n'.join(output))
