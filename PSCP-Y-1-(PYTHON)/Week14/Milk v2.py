"""Milk v2"""
def main(a,b,c,d,e):
    """Milk v2"""
    n=float(input())//a
    num1,num2=n,n
    k,k1=num1//b,num2//d
    while k>0 or k1>0:
        n+=k*c+k1*e
        num1+=k*(c - b)+k1*e
        num2+=k1*(e - d)+k*c
        k=num1//b
        k1=num2//d
    print(int(n))
main(float(input()),int(input()),int(input()),int(input()),int(input()))
