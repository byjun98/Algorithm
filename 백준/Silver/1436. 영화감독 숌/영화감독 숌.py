N = int(input())

count = 0
num = 666  # 종말의 수 시작점

while True:
    if "666" in str(num):  # 문자열로 변환해서 666 포함 여부 확인
        count += 1
        if count == N:
            print(num)
            break
    num += 1
