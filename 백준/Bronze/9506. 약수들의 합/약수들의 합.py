while True:
    n = int(input())

    if n == -1:
        break

    divisors = []
    
    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)

    if sum(divisors) == n:
        div_str = [str(d) for d in divisors]
        sum_expression = " + ".join(div_str)
        print(f"{n} = {sum_expression}")
    else:
        print(f"{n} is NOT perfect.")