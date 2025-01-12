"""CoinChange"""
def main():
    """CoinChange"""
    n = int(input())
    s=0
    n11 = n//11
    for i in range(1,n11+1):
        if not (n-(n11-i)*11)%7:
            n11-=1
            break
    n11 = 0 if n11<0 else n11
    s+=n11
    n7 = (n-n11*11)//7
    n7 = 0 if n7<0 else n7
    s+=n7
    n1 = n-n11*11-n7*7//1
    s+=n1
    print(s)
main()
