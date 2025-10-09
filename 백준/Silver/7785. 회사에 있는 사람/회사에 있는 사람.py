import sys
input = sys.stdin.readline

N = int(input())
people = set()

for _ in range(N):
    name, action = input().split()
    if action == 'enter':
        people.add(name)
    else:
        people.discard(name)

for name in sorted(people, reverse=True):
    print(name)
