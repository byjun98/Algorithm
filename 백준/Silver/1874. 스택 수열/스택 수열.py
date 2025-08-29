N = int(input())
num = [int(input()) for _ in range(N)]
stack = []
result = []
current = 1
st = True

for x in num:
    while current <= x:            # 목표 수까지 push
        stack.append(current)
        result.append('+')
        current += 1
    if stack[-1] == x:             # 원하는 수가 스택 top이면 pop
        stack.pop()
        result.append('-')
    else:                          # 아니면 불가능
        st = False
        break

if st:
    print('\n'.join(result))
else:
    print("NO")
