"""Rabbit"""
def main(x,y,n):
    """Rabbit"""
    if x>0 and y>0:
        if x<=n:
            num = (x*(x+1))//2
            x1=x
            if num > y:
                x = int((-1+(1+8*y)**0.5)//2)
                num = (x*(x+1))//2
            if x==n and num==y:
                print("Ahhahaha")
            else:
                print(x1-x,y-num,n-x)
        else:
            num = (n*(n+1))//2
            n1=n
            if num > y:
                n = int((-1+(1+8*y)**0.5)//2)
                num = (n*(n+1))//2
            print(x-n,y-num,n1-n)
    else:
        print("Ahhahaha")
main(int(input()),int(input()),int(input()))
