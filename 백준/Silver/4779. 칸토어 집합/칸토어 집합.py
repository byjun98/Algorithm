import sys
input = sys.stdin.readline

def cantor(arr, start, length):
    if length == 1:
        return
    third = length // 3

    for i in range(start + third, start + 2*third):
        arr[i] = ' '

    cantor(arr, start, third)
    cantor(arr, start + 2*third, third)

while True:
    try:
        N = int(input())
        arr = ['-'] * (3 ** N)
        cantor(arr, 0, 3 ** N)
        print(''.join(arr))
    except:
        break
