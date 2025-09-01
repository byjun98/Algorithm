N = int(input())
num = list(map(int, input().split()))
print(f"{sum(num)} {int(sum(num)/len(num))}")