t = int(input())
for i in range(t):
    U_num = int(input())
    max = 0
    m_name = ''
    for _ in range(U_num):
        name, num = input().split()
        num = int(num)
        if(num > max):
            max = num
            m_name = name
    print(m_name)