import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

# 중복 제거 후 정렬
sorted_unique = sorted(set(arr))

# 각 값의 압축 좌표 매핑
rank = {num: i for i, num in enumerate(sorted_unique)}

# 원래 배열에 매핑 적용
ans = [rank[x] for x in arr]

print(*ans)
