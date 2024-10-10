"""FibonacciRecursionV1"""
def fn(n):
    """FibonacciRecursionV1"""
    if n <= 1:
        return n
    return fn(n-1) + fn(n-2)
def main(n):
    """FibonacciRecursionV1"""
    t = fn(n)
    print(t)
main(int(input()))
