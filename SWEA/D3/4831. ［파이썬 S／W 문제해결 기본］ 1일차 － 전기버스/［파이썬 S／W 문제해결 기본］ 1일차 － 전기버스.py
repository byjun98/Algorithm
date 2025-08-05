T = int(input())
for t in range(1, T + 1):
    K, N, M = map(int, input().split())
    M_number = list(map(int,input().split()))    
    bus_stop = [0] * (N + 1)
    pos = 0
    cnt = 0
    
    for i in M_number:
        bus_stop[i] = 1
    
    while pos + K < N:
        for i in range(pos + K, pos, -1):
            if bus_stop[i] == 1:
                pos = i
                cnt += 1
                break
        else:
            cnt = 0
            break
    
    
    print(f"#{t} {cnt}")   