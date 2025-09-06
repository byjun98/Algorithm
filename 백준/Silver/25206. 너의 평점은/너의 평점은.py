total_score = 0
total_credit = 0

for t in range(20):
    O, S, P = input().split()
    S = float(S)
    if P == 'P':   # P는 계산 제외
        continue
    elif P == 'A+':
        total_score += S * 4.5
        total_credit += S
    elif P == 'A0':
        total_score += S * 4.0
        total_credit += S
    elif P == 'B+':
        total_score += S * 3.5
        total_credit += S
    elif P == 'B0':
        total_score += S * 3.0
        total_credit += S
    elif P == 'C+':
        total_score += S * 2.5
        total_credit += S
    elif P == 'C0':
        total_score += S * 2.0
        total_credit += S
    elif P == 'D+':
        total_score += S * 1.5
        total_credit += S
    elif P == 'D0':
        total_score += S * 1.0
        total_credit += S
    elif P == 'F':
        total_score += S * 0.0
        total_credit += S

print(total_score / total_credit)
