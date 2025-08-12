T = int(input())
for Tc in range(T):
    A, B, C = map(int, input().split())
    b = min(B, C - 1)          # B를 C-1로 맞춤(넘으면 내림)
    a = min(A, b - 1)          # A를 b-1로 맞춤(넘으면 내림)
    if a >= 1 and b >= 2 and a < b < C:
        print(f'#{Tc+1} {(B - b) + (A - a)}')
    else:
        print(f'#{Tc+1} -1')