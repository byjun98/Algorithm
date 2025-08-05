T = 10
for t in range(1, T + 1):
    dump = int(input())
    data = list(map(int, input().split()))
    
    while dump > 0:
        min_box = 0
        max_box = 0
        for i in range(len(data)):
            if data[max_box] < data[i]:
                max_box = i
            if data[min_box] > data[i]:
                min_box = i
                
        if data[max_box] - data[min_box] <= 1:
            break
                        
        data[max_box] -= 1
        data[min_box] += 1
        dump -= 1
    
    min_box = 0
    max_box = 0
    for i in range(len(data)):
        if data[max_box] < data[i]:
            max_box = i
        if data[min_box] > data[i]:
            min_box = i
    
    boxes = data[max_box] - data[min_box]
    print(f"#{t} {boxes}")
