num = []
for _ in range(9):
    num.append(int(input()))

total = sum(num)
a, b = 0, 0

# 두 명 찾기
for i in range(9):
    for j in range(i+1, 9):
        if total - (num[i] + num[j]) == 100:
            a, b = i, j
            break
    if a or b:
        break

# 일곱 난쟁이 출력
for k in range(9):
    if k != a and k != b:
        print(num[k])
