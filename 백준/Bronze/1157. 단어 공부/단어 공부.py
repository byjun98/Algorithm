arr = input().strip()
arr = arr.upper()
al = [0] * 26
cnt = 0
k = False
for i in range(len(arr)):
    idx = ord(arr[i])- ord('A')
    al[idx] += 1
max_al = max(al)

for i in range(len(al)):
    if al[i] == max_al:
        cnt += 1
        if cnt < 2:
            K = True
            result = chr(65+i)
        else: K = False
if K :
    print(result)
else: print('?')