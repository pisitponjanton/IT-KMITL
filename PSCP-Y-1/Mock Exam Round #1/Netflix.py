"""Netflix"""
def f2(num):
    """f2"""
    dum=0
    nn1=num//2
    nn2=num-nn1*2
    dum+=nn1*349
    if nn1>0:
        print(f"Standard x {nn1}")
    if nn2>0:
        print(f"Basic x {nn2}")
        dum+=nn2*279
    return dum
def f3(num):
    """f3"""
    dum=0
    n1n = num//4
    n2n = num-n1n*4
    if n2n==3:
        n1n+=1
    if num>0:
        print(f"Premium x {n1n}")
    dum+=419*n1n
    if 0<n2n<3:
        dum+=f2(n2n)
    return dum
def f4(num):
    """f4"""
    dum=0
    nnl1=num//4
    nnl2=num - nnl1*4
    if nnl2==3:
        nnl1+=1
    print(f"Premium x {nnl1}")
    dum+=419*nnl1
    if 0<nnl2<=2:
        print(f"Standard x {1}")
        dum+=349
    return dum
def f5(num):
    """f5"""
    dum=0
    if num<=4:
        print(f"Premium x {1}")
        dum+=419
    elif not num%4:
        print(f"Premium x {num//4}")
        dum+=419*(num//4)
    else:
        print(f"Premium x {(num//4)+1}")
        dum+=419*((num//4)+1)
    return dum
def netflix():
    """Netflix"""
    n = ""
    dum = 0
    num1 = int(input())
    num2 = int(input())
    for _ in range(5):
        n1 = input()
        n+= "1"if n1 == "Yes" else "0"
    if n in ("11000","10000","01000","00000"):
        numm = num1 if num1>=num2 else num2
        print(f"Mobile x {numm}")
        dum+=99*numm
    elif n in ("11100","10100","01100","00100"):
        if num1==1 and num2==1:
            print(f"Basic x {num1}")
            dum+=279*num1
        elif num1<3 and num2<3:
            dum+= f2(num1) if num1 >= num2 else f2(num2)
        else:
            dum+=f3(num1) if num1 >= num2 else f3(num2)
    elif n in ("11110","11010","10110","10010","01110","01010","00110","00010"):
        if num1<=2 and num2<=2:
            print(f"Standard x {1}")
            dum+=349
        elif 2<num1<=4 and 2<num2<=4:
            print(f"Premium x {1}")
            dum+=419
        else:
            dum+= f4(num1) if num1>=num2 else f4(num2)
    else:
        dum+= f5(num1)if num1>=num2 else f5(num2)
    print(f"Total = {dum} THB")
netflix()
