import sys
input = sys.stdin.readline

while True:
    line = input().rstrip()
    if line == '.':
        break

    stack = []
    balanced = True

    for ch in line:
        if ch in '([':
            stack.append(ch)
        elif ch == ')':
            if not stack or stack[-1] != '(':
                balanced = False
                break
            stack.pop()
        elif ch == ']':
            if not stack or stack[-1] != '[':
                balanced = False
                break
            stack.pop()
        # 알파벳, 공백, 점 등은 무시

    if balanced and not stack:
        print("yes")
    else:
        print("no")
