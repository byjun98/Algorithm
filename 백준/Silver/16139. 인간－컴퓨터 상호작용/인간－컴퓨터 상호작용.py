import sys
input = sys.stdin.readline

S = list(input().strip())
q = int(input())
al = [0] * 26
for i in range(q):
    cnt = 0
    cl = list(input().split())
    for j in range(int(cl[1]), int(cl[2])+1):
        if ord(S[j]) == ord(cl[0]):
            cnt += 1
    print(cnt)