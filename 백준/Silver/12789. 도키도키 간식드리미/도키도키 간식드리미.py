import sys
input = sys.stdin.readline

N = int(input())
line = list(map(int, input().split()))

stack = []
current = 1  # 다음 번호

for person in line:
    # 스택의 맨 위가 다음 번호면 계속 pop
    while stack and stack[-1] == current:
        stack.pop()
        current += 1

    if person == current:
        current += 1
    else:
        stack.append(person)

# 모든 줄이 끝난 후 스택에 남은 사람도 확인
while stack and stack[-1] == current:
    stack.pop()
    current += 1

if current == N + 1:
    print("Nice")
else:
    print("Sad")
