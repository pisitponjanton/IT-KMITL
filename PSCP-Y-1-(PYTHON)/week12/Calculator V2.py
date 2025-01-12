"""Calculator V2"""
def main():
    """Calculator V2"""
    s=0
    n=int(input())
    m=len(str(n))
    x = abs((n - int("1"+("0"*(m-1)))))+1
    for i in range(1,m):
        s+= int("9"+("0"*(i-1)))*(i+1)
    s+=x*(m+1)
    print(s if s!=2 else 1)
main()
