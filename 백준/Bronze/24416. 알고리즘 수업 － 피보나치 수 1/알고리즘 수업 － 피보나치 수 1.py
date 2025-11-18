n = int(input())

fib = [0] * (n+1)
fib[1] = fib[2] = 1
for i in range(3, n+1):
    fib[i] = fib[i-1] + fib[i-2]

code1 = fib[n]
code2 = n - 2

print(code1, code2)
