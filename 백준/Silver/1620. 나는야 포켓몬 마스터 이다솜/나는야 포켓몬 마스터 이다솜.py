import sys

input = sys.stdin.readline

n, m = map(int, input().split())

pokedex_by_num = []

pokedex_by_name = {}

for i in range(1, n + 1):
    name = input().strip()
    pokedex_by_num.append(name)
    pokedex_by_name[name] = i

for _ in range(m):
    query = input().strip()
    if query.isdigit():
        print(pokedex_by_num[int(query) - 1])
    else:
        print(pokedex_by_name[query])