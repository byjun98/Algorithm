T = int(input())
for t in range(1, T + 1):
    tokens = input().split()
    stack = []
    error_flag = False

    for token in tokens:
        if token.isdigit():  # 숫자
            stack.append(int(token))
        elif token in ['+', '-', '*', '/']:
            if len(stack) < 2:
                error_flag = True
                break
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a // b)
        elif token == '.':
            if len(stack) != 1:
                error_flag = True
            break
        else:  # 알 수 없는 토큰
            error_flag = True
            break

    if error_flag:
        print(f"#{t} error")
    else:
        print(f"#{t} {stack[0]}")
