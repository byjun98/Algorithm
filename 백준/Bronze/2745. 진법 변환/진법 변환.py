N, B = input().split()
B = int(B)

digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
value_map = {ch: i for i, ch in enumerate(digits)}

result = 0
for ch in N:
    result = result * B + value_map[ch]

print(result)
