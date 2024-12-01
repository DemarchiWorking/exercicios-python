import sys

def recursive_factorial(n):
    if n == 0:
        return 1
    return n * recursive_factorial(n - 1)

#sys.setrecursionlimit(2500)

try:
    print(recursive_factorial(999))
except RecursionError:
    print("Stack Overflow occurred")
