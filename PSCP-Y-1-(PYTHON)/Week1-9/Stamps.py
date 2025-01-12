"""Stamps"""
def main():
    """Stamps"""
    n = int(input())
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    s=0
    dde=0
    num = 0
    for _ in range(n):
        buy=int(input())
        if dde<=buy:
            num+=buy-dde
            s+=((buy-dde)//a)*b
            dde=(s//c)*d
        else:
            l =  0 if not buy%d else 1
            dde-=((buy//d)+l)*d
        s-=(s//c)*c
    s+=(dde//d)*c if d else 0
    print(num)
    print(s)
main()
