"""OTP"""
def main():
    """OTP"""
    l=[]
    while True:
        n = input()
        a,b=[],''
        if n == "0":
            break
        for i in n:
            a.append(n.count(i))
        a.sort()
        for i in a:
            b+="".join(str(i))
        if len(n)==8:
            l.append("Valid" if b in ("11222222","11333333","22333333") else "Invalid")
        else:
            l.append("Valid" if b in ("1122","112222","111333",'122333') else "Invalid")
    for i in l:
        print(i)
main()
