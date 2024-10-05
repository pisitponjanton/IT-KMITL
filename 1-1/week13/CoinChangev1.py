"""CoinChangev1"""
def main():
    """CoinChangev1"""
    n = int(input())
    s=0
    n1=n//25
    s+=n1 if n1 > 0 else 0
    n2=(n-n1*25)//10
    s+=n2 if n2 > 0 else 0
    n3= (n-n1*25-n2*10)//5
    s+=n3 if n3 >0 else 0
    n4= (n-n1*25-n2*10-n3*5)//1
    s+=n4 if n4 >0 else 0
    print(s)
main()
