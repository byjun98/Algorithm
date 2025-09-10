def merge(left, right):
    result = [0] * (len(left) + len(right))
    l = r = 0

    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result[l + r] = left[l]
            l +=1
        else:
            result[l + r] = right[r]
            r += 1
    while l < len(left):
        result[l + r] = left[l]
        l += 1
    while r < len(right):
        result[l + r] = right[r]
        r += 1
    return result

def merge_sort(li):
    global cnt
    if len(li) == 1:
        return li
    mid = len(li) // 2
    left = li[:mid]
    right = li[mid:]

    left_list = merge_sort(left)
    right_list = merge_sort(right)
    if left_list[-1] > right_list[-1]:
        cnt += 1

    merge_list = merge(left_list, right_list)
    return merge_list


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    num = list(map(int, input().split()))
    cnt = 0
    sorted_arr = merge_sort(num)
    print(f"#{t} {sorted_arr[N // 2]} {cnt}")