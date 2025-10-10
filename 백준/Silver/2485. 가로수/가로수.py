import sys
input = sys.stdin.readline

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

N = int(input())
trees = [int(input()) for _ in range(N)]

diffs = [trees[i+1] - trees[i] for i in range(N-1)]

g = diffs[0]
for d in diffs[1:]:
    g = gcd(g, d)

new_trees = (trees[-1] - trees[0]) // g - (N - 1)
print(new_trees)
