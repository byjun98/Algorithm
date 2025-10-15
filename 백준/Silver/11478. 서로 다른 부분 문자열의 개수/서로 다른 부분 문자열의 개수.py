import sys
input = sys.stdin.readline

arr = input().strip()
lst = []

for i in range(len(arr)):
    for j in range(len(arr)):
        if len(arr[i:j+1]) == 0:
            continue
        else:
            lst.append(arr[i:j+1])
print(len(set(lst)))

