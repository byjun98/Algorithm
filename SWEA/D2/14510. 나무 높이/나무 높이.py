T = int(input())
for t in range(1, T+1):
    N = int(input())
    trees = list(map(int, input().split()))
    max_h = max(trees)

    # 1. 각 나무의 부족한 높이 차이
    diff = [max_h - h for h in trees]

    # 2. 홀수(1cm) 작업 수, 짝수(2cm) 작업 수 계산
    ones, twos = 0, 0
    for d in diff:
        twos += d // 2
        ones += d % 2

    # 3. 짝수 작업이 많을 때 조정
    while twos > ones + 1:
        twos -= 1
        ones += 2

    # 4. 전체 날짜 계산
    if twos >= ones:
        days = twos * 2
    else:
        days = ones * 2 - 1

    print(f"#{t} {days}")
