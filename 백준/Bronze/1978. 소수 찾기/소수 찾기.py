N = int(input())
arr = list(map(int, input().split()))
num = []
cnt = 0

for x in arr:                        # arr의 원소 하나씩
    if x < 2:
        continue
    is_prime = True
    for i in range(2, int(x**0.5)+1):  # 2부터 √x까지
        if x % i == 0:
            is_prime = False
            break
    if is_prime:
        num.append(x)
        cnt += 1

print(cnt)
