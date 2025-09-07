N = int(input())

line = 0  # 대각선 번호
cnt = 0   # 누적 개수

# N이 속한 대각선 찾기
while cnt < N:
    line += 1
    cnt += line

# line번째 대각선의 몇 번째 항인지
idx = N - (cnt - line)

if line % 2 == 0:  # 짝수 대각선: 위→아래
    num = idx
    den = line - idx + 1
else:              # 홀수 대각선: 아래→위
    num = line - idx + 1
    den = idx

print(f"{num}/{den}")
