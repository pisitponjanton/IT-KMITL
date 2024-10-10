"""FibonacciRecursionV2"""
def fn1(n,memo,i):
    """FibonacciRecursionV2"""
    fn(i,memo)
    if 996<=i<n:
        i+=800
        return fn1(n,memo,i)
    return i
def fn(n, memo):
    """FibonacciRecursionV2"""
    if n in memo:
        return memo[n]
    if n<=1:
        return n
    memo[n] = fn(n-1,memo)+fn(n-2,memo)
    return memo[n]
def main(n):
    """FibonacciRecursionV2"""
    memo = {}
    i=996
    if n>=996:
        fn1(n,memo,i)
    t=fn(n,memo)
    print(t)
main(int(input()))
