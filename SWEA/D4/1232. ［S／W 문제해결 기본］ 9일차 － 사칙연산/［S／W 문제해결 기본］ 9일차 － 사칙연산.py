def evaluate(node):
    value, left, right = tree[node]
    if left is None:  # 숫자 노드
        return float(value)
    else:  # 연산자 노드
        lval = evaluate(left)
        rval = evaluate(right)
        if value == '+':
            return lval + rval
        elif value == '-':
            return lval - rval
        elif value == '*':
            return lval * rval
        elif value == '/':
            return lval / rval

for tc in range(1, 11):  # 문제에서 테스트케이스 10개 고정
    N = int(input())
    tree = {}

    for _ in range(N):
        parts = input().split()
        idx = int(parts[0])
        if len(parts) == 2:  # 숫자 노드
            tree[idx] = (parts[1], None, None)
        else:  # 연산자 노드
            op, l, r = parts[1], int(parts[2]), int(parts[3])
            tree[idx] = (op, l, r)

    result = evaluate(1)  # 루트부터 계산
    print(f"#{tc} {int(result)}")  # 소수점 버림
