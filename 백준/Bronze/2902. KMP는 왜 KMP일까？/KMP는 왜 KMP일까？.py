arr = [t for t in input().strip().split('-')]
r = []
for i in range(len(arr)):
    r.append(arr[i][0])
print(''.join(r))
