def inorder(idx):
    global num
    if idx <= N:
        inorder(idx*2)           # 왼쪽
        tree[idx] = num          # 현재 노드 채우기
        num += 1
        inorder(idx*2+1)         # 오른쪽

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = [0] * (N+1)
    num = 1
    inorder(1)
    print(f"#{tc} {tree[1]} {tree[N//2]}")
