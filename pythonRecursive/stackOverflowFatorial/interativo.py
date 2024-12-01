def iterative_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(iterative_factorial(1500))
