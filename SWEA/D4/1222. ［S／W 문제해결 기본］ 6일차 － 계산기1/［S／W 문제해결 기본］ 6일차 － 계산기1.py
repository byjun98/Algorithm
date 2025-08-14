T = 10
for t in range(1, T + 1):
    n = int(input())
    infix = input().strip()

    # 1. 중위  후위 변환
    postfix = ""
    stack = []
    for ch in infix:
        if ch.isdigit():
            postfix += ch
        else:  # '+'
            stack.append(ch)
    # 스택에 남은 연산자 추가
    while stack:
        postfix += stack.pop()

    # 2. 후위식 계산
    calc_stack = []
    for ch in postfix:
        if ch.isdigit():
            calc_stack.append(int(ch))
        else:  # '+'
            b = calc_stack.pop()
            a = calc_stack.pop()
            calc_stack.append(a + b)

    result = calc_stack[0]
    print(f"#{t} {result}")
