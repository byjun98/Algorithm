S = int(input())
if S % 4 == 0 and S % 100 != 0 or S % 400 == 0:
    print(1)
else:
    print(0)