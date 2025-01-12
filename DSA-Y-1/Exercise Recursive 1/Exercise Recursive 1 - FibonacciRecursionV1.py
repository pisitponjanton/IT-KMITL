"""Exercise Recursive 1 - FibonacciRecursionV1"""
def fibonacci(x):
    """Fibonacci"""
    if x>1:
        return fibonacci(x-1) + fibonacci(x-2)
    else:
        return x
def main():
    """main"""
    print(fibonacci(int(input())))
main()