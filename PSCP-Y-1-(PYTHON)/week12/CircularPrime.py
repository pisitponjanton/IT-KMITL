"""CircularPrime"""
def o(x):
    """int(n**0.5) + 1"""
    t=True
    for i in range(2,int(x**0.5)+1):
        if not x%i:
            t=False
            break
    if t:
        return 1
    return 0
def f(n):
    """CircularPrime"""
    n=str(n)
    m=len(n)
    k=n
    s=0
    for _ in range(m):
        k=k[1:]+k[0]
        s+=o(int(k))
    if s==m:
        return int(n)
    return 0
def main():
    """CircularPrime"""
    n=0
    t=int(input())
    for i in range(3,t+1):
        r = True
        for j in range(2,int(i**0.5)+1):
            if not i%j:
                r=False
                break
        if r:
            n+=f(i)
    print(n+2 if t>=2 else n )
main()
