import sys
input = sys.stdin.readline

N = int(input())
arr1 = list(map(int, input().split()))
M = int(input())
arr2 = list(map(int, input().split()))

# arr1의 등장 횟수 저장
count_dict = {}
for x in arr1:
    if x in count_dict:
        count_dict[x] += 1
    else:
        count_dict[x] = 1

# arr2의 각 원소에 대해 출력
ans = [count_dict.get(x, 0) for x in arr2]
print(*ans)
