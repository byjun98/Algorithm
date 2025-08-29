def heap_push(heap, value):
    heap.append(value)
    i = len(heap) - 1
    while i > 1 and heap[i] < heap[i//2]:
        heap[i], heap[i//2] = heap[i//2], heap[i]
        i //= 2

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    heap = [0]  # 0번은 비워둠
    for val in arr:
        heap_push(heap, val)

    # 마지막 노드 번호 = N
    idx = N
    total = 0
    while idx > 1:
        idx //= 2
        total += heap[idx]

    print(f"#{tc} {total}")
