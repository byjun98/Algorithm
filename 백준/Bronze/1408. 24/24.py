H, M, S = map(int, input().split(':'))
EH, EM, ES = map(int, input().split(':'))

# 현재 시각과 임무 시작 시각을 초 단위로 변환
cur = H*3600 + M*60 + S
start = EH*3600 + EM*60 + ES

# 남은 시간 (24시간 = 86400초)
remain = (start - cur) % (24*3600)

# 시, 분, 초로 변환
RH = remain // 3600
RM = (remain % 3600) // 60
RS = remain % 60

# 두 자리 형식으로 출력
print(f"{RH:02d}:{RM:02d}:{RS:02d}")
