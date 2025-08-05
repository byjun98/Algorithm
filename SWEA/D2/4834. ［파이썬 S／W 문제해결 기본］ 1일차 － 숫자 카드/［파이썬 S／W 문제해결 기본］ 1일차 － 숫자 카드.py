T = int(input())
for t in range(1, T + 1):
    card = int(input())
    n = list(map(int, input()))
    c = [0] * 10
     
    for i in n:
        c[i] += 1
         
    max_count = max(c)
    max_num = -1
     
    for i in range(9, -1, -1):
        if c[i] == max_count:
            max_num = i
            break
     
    print(f"#{t} {max_num} {max_count}")
