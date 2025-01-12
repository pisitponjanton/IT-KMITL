"""[Final 2020] Bus Seat"""
def main(n,m,x):
    """[Final 2020] Bus Seat"""
    n2=n
    for i in range(1,n+1):
        n1=n2
        for _ in range(m):
            if n1==x:
                print("XX",end=" ")
            else:
                print(f"{n1:02d}",end=" ")
            n1+=n
        print()
        if not i%2 and i and i!=n:
            print()
        n2-=1
main(int(input()),int(input()),int(input()))
