"""Bubble"""
def main():
    """Bubble"""
    t = input()
    n=0
    n1=0
    s=0
    k=0
    o=0
    s1=0
    for i in t:
        k=0 if s1 == s else k
        if k:
            s+=1
            continue
        if o or i.isspace():
            o=1
            n1+=1
            continue
        if i == "O":
            if t[s+1] == "|":
                n+=2
                break
            if t[s+2] == "|":
                n+=2
                break
            if t[s+3] == "|":
                n+=2
                break
            if t[s+3] in ("O","|"):
                k=1
                s1=s+3
            elif t[s+2] in ("O","|"):
                k=1
                s1=s+2
            elif t[s+1] in ("O","|"):
                k=1
                s1=s+1
            elif t[s+3] in ("o","|"):
                k=1
                s1=s+3
            elif t[s+3] == " ":
                o=1
        s+=1
        n+=1
    print("POSSIBLE" if not o else "IMPOSSIBLE")
    print(n-1 if not o else n1)
main()
