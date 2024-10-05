"""Volleyball"""
def cont14(x,a,b):
    """cont"""
    if x == "A":
        a+=1
    elif x == "B":
        b+=1
    return a,b
def setab(a,b,seta,setb):
    """setA-setB"""
    if a>b:
        seta+=1
    elif a<b:
        setb+=1
    return seta,setb
def won(a,b):
    """WINWONWON"""
    s=""
    fo = ""
    bo = ""
    if a>b:
        s="A"
        fo = a
        bo = b
    elif b>a:
        s="B"
        fo = b
        bo = a
    return fo,bo,s
def main():
    """Volleyball"""
    text = input()
    sa = 0
    sb = 0
    na=0
    nb=0
    n=1
    dd = ""
    for i in text:
        na,nb = cont14(i,na,nb)
        if dd == "Dew":
            if abs(na-nb)>=2:
                dd=""
        if na == 24 and nb == 24 and n<=4 and not dd:
            dd="Dew"
        elif (na>=25 or nb>=25) and n<=4 and not dd:
            sa,sb = setab(na,nb,sa,sb)
            print(f"Set {n}: A ({na}) | B ({nb})")
            na=0
            nb=0
            n+=1
        if sa==sb and n==5:
            if na == 14 and nb == 14 and not dd:
                dd="Dew"
            elif (na>=15 or nb>=15) and not dd:
                sa,sb = setab(na,nb,sa,sb)
                print(f"Set {n}: A ({na}) | B ({nb})")
        if sa >= 3 or sb >= 3:
            break
    b1 = dd == "Dew" or n<=5
    b2 = sa != 3 and sb != 3
    if 1<=n<=5 and (sa != 3  and sb != 3):
        print(f"Set {n}: A ({na}) | B ({nb})")
    if b1 and b2:
        print("The game has not finished yet.")
    if sa == 3 or sb == 3:
        f,b,ab = won(sa,sb)
        print(f"{ab} won {f}:{b} set")
main()
