import sys
input = sys.stdin.readline

def draw_star(n):
    # 기본 패턴 (3x3)
    if n == 3:
        return ['***', '* *', '***']

    prev = draw_star(n // 3)  # 이전 단계(더 작은 패턴)
    stars = []

    # 3개의 블록으로 나눠서 구성
    for i in range(3):
        for line in prev:
            if i == 1:  # 가운데 줄
                stars.append(line + ' ' * (n // 3) + line)
            else:       # 위, 아래 줄
                stars.append(line * 3)

    return stars


N = int(input())
result = draw_star(N)
print('\n'.join(result))
