N = int(input())

layer = 1
end = 1  # 각 층의 마지막 방 번호

while N > end:
    end += 6 * layer
    layer += 1

print(layer)
