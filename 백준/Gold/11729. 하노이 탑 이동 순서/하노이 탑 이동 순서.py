import sys
input = sys.stdin.readline

def hanoi(n, start, target, via):
    if n == 1:
        result.append((start, target))
        return
    hanoi(n - 1, start, via, target)   # 1단계
    result.append((start, target))     # 2단계
    hanoi(n - 1, via, target, start)   # 3단계

N = int(input())
result = []
hanoi(N, 1, 3, 2)

print(len(result))
for a, b in result:
    print(a, b)
