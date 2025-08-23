max_people = 0
people = 0
for t in range(10):
    O, I = map(int, input().split())
    people -= O
    people += I
    if people > max_people:
        max_people = people
print(max_people)