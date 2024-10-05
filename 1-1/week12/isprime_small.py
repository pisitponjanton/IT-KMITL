"""isprime_small"""
def is_prime():
    """is_prime()"""
    x = int(input())
    n=0
    for i in range(x-1,1,-1):
        if not x%i:
            n=1
            break
    return n,x
def main():
    """isprime_small"""
    n,x = is_prime()
    print("Yes" if not n and x!=1 else "No")
main()
