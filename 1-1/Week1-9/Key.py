"""Key"""
def main():
    """Key"""
    num = input()
    n1 = 0
    for i in num:
        n1+=int(i)
    n2 = int(num[-3:]+"0")
    sn = n1+n2
    print(sn+1000 if sn < 1000 else str(sn)[-4:] if sn >= 10000 else sn)
main()
