def tail_recursive_factorial(n, accumulator=1):
    if n == 0:
        return accumulator
    return tail_recursive_factorial(n - 1, accumulator * n)

try:
    print(tail_recursive_factorial(1500))
except RecursionError:
    print("Stack Overflow occurred, even with tail recursion in Python")
