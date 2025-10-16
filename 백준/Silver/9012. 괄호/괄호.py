import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    stack = []
    s = input().strip()
    is_vps = True  # 일단 맞다고 가정

    for ch in s:
        if ch == '(':
            stack.append(ch)
        else:  # ch == ')'
            if stack:        # 스택에 '('가 남아 있다면 짝 지움
                stack.pop()
            else:            # 짝이 없는데 ')'가 나오면 바로 실패
                is_vps = False
                break

    # 끝났을 때 스택이 비어있어야 완전한 VPS
    if is_vps and not stack:
        print("YES")
    else:
        print("NO")
