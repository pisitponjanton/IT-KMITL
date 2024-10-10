"""Bubble"""
def main():
    """Bubble"""
    t = input().strip()
    n=0
    m=""
    nr = 0
    ns=0
    nm=0
    for i in t:
        if i.isspace() and not nr:
            m="im"
        if m == "im":
            nm+=1
        if i == "O":
            if t[ns+1] == "|":
                n+=1
                if not nr:
                    n+=1
                break
            if t[ns+2]=="|":
                n+=2
                break
            if t[ns+3] == "O":
                n-=2
            elif t[ns+2] == "O":
                n-=1
            elif t[ns+3] == " ":
                if t[ns+2] == "O":
                    n-=1
                elif t[ns+1] == "O":
                    pass
                elif t[ns+2] == "o":
                    nm-=1
                elif t[ns+1] == "o":
                    nm+=0
                else:
                    m="im"
                    nm-=2
            else:
                n-=2
            nr=ns #แก้ตรงนี้
        if ns == nr+3:
            nr=0
        ns+=1
        n+=1
    print("IMPOSSIBLE" if m=="im" else "POSSIBLE")
    print(nm if m=="im" else n-1)
main()
