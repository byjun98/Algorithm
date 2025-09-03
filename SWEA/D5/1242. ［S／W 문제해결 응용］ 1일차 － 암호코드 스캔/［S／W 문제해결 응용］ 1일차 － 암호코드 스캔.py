# 7비트  숫자
pattern_map = {
    "0001101": 0, "0011001": 1, "0010011": 2,
    "0111101": 3, "0100011": 4, "0110001": 5,
    "0101111": 6, "0111011": 7, "0110111": 8,
    "0001011": 9
}

# 7비트 패턴을 '오른쪽에서부터 1-0-1 구간 길이 비율(=c3,c2,c1)'로 변환한 매핑
ratio_to_digit = {}
for bits, d in pattern_map.items():
    j = len(bits) - 1
    c1 = c2 = c3 = 0
    while j >= 0 and bits[j] == '1':  # 마지막 1들의 길이
        c1 += 1; j -= 1
    while j >= 0 and bits[j] == '0':  # 그 앞 0들의 길이
        c2 += 1; j -= 1
    while j >= 0 and bits[j] == '1':  # 그 앞 1들의 길이
        c3 += 1; j -= 1
    ratio_to_digit[(c3, c2, c1)] = d

# 16진수  2진수
hex_to_bin = {
    '0': "0000", '1': "0001", '2': "0010", '3': "0011",
    '4': "0100", '5': "0101", '6': "0110", '7': "0111",
    '8': "1000", '9': "1001", 'A': "1010", 'B': "1011",
    'C': "1100", 'D': "1101", 'E': "1110", 'F': "1111"
}

def check_code(d):
    # d: 길이 8 리스트
    return ((d[0] + d[2] + d[4] + d[6]) * 3 + (d[1] + d[3] + d[5]) + d[7]) % 10 == 0

T = int(input().strip())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    rows_hex = [input().strip().upper() for _ in range(N)]

    # 16진수  2진수 문자열
    rows_bin = ["".join(hex_to_bin[ch] for ch in line) for line in rows_hex]

    seen_codes = set()
    total = 0

    for i in range(N):
        s = rows_bin[i]
        prev = rows_bin[i - 1] if i > 0 else "0" * len(s)
        j = len(s) - 1

        while j >= 55:  # 최소 56비트가 남아야 8자리 가능
            if s[j] == '0':
                j -= 1
                continue

            # 같은 코드 세로 중복 방지: 위 줄이 1이면 건너뜀
            if prev[j] == '1':
                j -= 1
                continue

            digits = []
            ok = True

            # 오른쪽 끝에서 왼쪽으로 8자리 디코딩
            for _ in range(8):
                c1 = c2 = c3 = 0

                # 1들의 길이
                while j >= 0 and s[j] == '1':
                    c1 += 1; j -= 1
                # 0들의 길이
                while j >= 0 and s[j] == '0':
                    c2 += 1; j -= 1
                # 1들의 길이
                while j >= 0 and s[j] == '1':
                    c3 += 1; j -= 1

                if c1 == 0 or c2 == 0 or c3 == 0:
                    ok = False
                    break

                k = min(c1, c2, c3)
                key = (c3 // k, c2 // k, c1 // k)
                d = ratio_to_digit.get(key)
                if d is None:
                    ok = False
                    break

                digits.append(d)

                # 자리 사이 구분용 0들 스킵
                while j >= 0 and s[j] == '0':
                    j -= 1

            if ok and len(digits) == 8:
                digits.reverse()  # 오른쪽왼쪽으로 읽었으니 뒤집기
                t = tuple(digits)
                if t not in seen_codes and check_code(digits):
                    total += sum(digits)
                    seen_codes.add(t)
            # 실패했어도 j는 이미 왼쪽으로 이동돼 있으니 다음 루프로 진행

    print(f"#{tc} {total}")
