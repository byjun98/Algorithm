T = int(input())
for t in range(1, T + 1):
    N = int(input())
    row = [1]
    print(f"#{t}")
    for i in range(N):
        print(*row)
        new_row = [1]
        for j in range(1, len(row)):
            new_row.append(row[j-1] + row[j])
        new_row.append(1)
        row = new_row


