T = int(input())
for t in range(1, T + 1):
    s = input().strip()
    top = -1
    stack = [0] * 1000
    for x in s:
        if top >= 0 and stack[top] == x:
            top -= 1
        else:
            top += 1
            stack[top] = x

    result_len = top + 1

    print(f"#{t} {result_len}")