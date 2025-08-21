T = int(input())
people = []

for _ in range(T):
    name, day, month, year = input().split()
    day, month, year = int(day), int(month), int(year)
    people.append((year, month, day, name))

people.sort()

print(people[-1][3])

print(people[0][3])


