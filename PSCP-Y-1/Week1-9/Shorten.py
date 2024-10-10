"""Shorten"""
def main():
    """Shorten"""
    num = int(input())
    t= str(num)
    f = num
    i=num
    while num!=-1:
        num = int(input())
        if abs(f-num)>1:
            if num == -1:
                p = ""
            else:
                p = ", "+str(num)
            if i == f :
                g = ""
            else:
                g = "-"+str(f)
            t+=g+p
            i = num
        f = num
    print(t if t != "-1" else '')
main()
