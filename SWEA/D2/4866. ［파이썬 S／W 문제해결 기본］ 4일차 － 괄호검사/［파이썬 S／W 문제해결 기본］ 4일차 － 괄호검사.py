T = int(input())
for t in range(1, T + 1):
    s = input().strip()
    top = -1
    stack = [0] * 100
    ans = 1

    pairs = {')': '(', ']': '[', '}': '{'}

    for x in s:
        if x in ['(', '{', '[']:
            top += 1
            stack[top] = x
        elif x in [')', '}', ']']:
            if top == -1 or stack[top] != pairs[x]:
                ans = 0
                break
            top -= 1
        else:
            pass
        
    if top != -1:
        ans = 0

    print(f"#{t} {ans}")
