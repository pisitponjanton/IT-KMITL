"""IT Business"""
def main():
    """IT Business"""
    kb = float(input())
    kw = float(input())
    n = ""
    e = 0
    while n != "end":
        if e == 3:
            break
        n = input()
        if n[0] == "D":
            if kw >= float(n[2:]):
                kb+=float(n[2:])
                kw-=float(n[2:])
                e=0
            else:
                e+=1
        elif n[0] == "W":
            if kb >= float(n[2:]):
                kw+=float(n[2:])
                kb-=float(n[2:])
                e=0
            else:
                e+=1
    print(f"{kb:.2f}\n{kw:.2f}")
main()
