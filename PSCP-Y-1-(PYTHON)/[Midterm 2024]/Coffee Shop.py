"""Coffee Shop"""
def n1(a1,b1,e1):
    """Coffee Shop"""
    nume = a1*e1
    nume -= (b1/100)*(a1*(e1-1))
    return nume
def n2(a2,c2,d2,e2):
    """Coffee Shop"""
    num = a2*e2
    if a2*e2 >= d2:
        num -= (c2/100)*num
    return num
def main():
    """Coffee Shop"""
    a = float(input())
    b = float(input())
    c = float(input())
    d = float(input())
    e = int(input())
    num1 = n1(a,b,e)
    num2 = n2(a,c,d,e)
    print(1 if num1<num2 else 2)
    print(f"{num1:.2f}" if num1<num2 else f"{num2:.2f}")
main()
