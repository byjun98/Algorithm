while True:
    a, b, c = map(int, input().split())
    if a == 0:
        exit()
    m = max(a, b, c)
    if a+b+c-m <= m:
        print('Invalid')
    elif a==b==c:
        print('Equilateral ')
    elif a==b or b==c or a==c:
        print('Isosceles ')
    else:
        print('Scalene ')