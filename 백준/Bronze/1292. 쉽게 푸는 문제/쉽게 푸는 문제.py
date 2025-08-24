A, B = map(int, input().split())

seq = []
for i in range(1, B+1):     # B번째 원소까지는 커버하도록
    seq.extend([i] * i)     # 숫자 i를 i번 추가

print(sum(seq[A-1:B]))      # A번째~B번째 원소 합
