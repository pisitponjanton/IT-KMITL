"""MAC"""
def sx(x,y):
    """s"""
    v=""
    k=0
    for i in x:
        if x[0]== "-":
            if i!="-" or len(y)!=17 or len(x)!=5:
                v="ERROR"
                break
            k=1
        elif x[0]== ":":
            if i!=":" or len(y)!=17 or len(x)!=5:
                v="ERROR"
                break
            k=2
        elif x[0]== ".":
            if i!="." or len(y)!=14 or len(x)!=2:
                v="ERROR"
                break
            k=3
    return k,v
def af(x):
    """A-F"""
    u=""
    v=""
    af1 = ["A","B","C","D","E","F",
          "a","b","c","d","e","f"]
    for i in x:
        if i.isalpha():
            u+=i
    for i in u:
        if not i in af1:
            v = "ERROR"
    return v
def main():
    """MAC"""
    t = input()
    s=""
    y=0
    n=0
    for i in t:
        if not i.isalnum():
            s+=i
        if i.isspace():
            g="ERROR"
            break
    r,g = sx(s,t)
    if not g:
        g = af(t)
    s=""
    y = 4 if r == 3 else 2
    for i in t:
        s+=i
        if n==y:
            # print(s)
            if s[y] in (".",":","-"):
                s=""
                n=-1
            else:
                g="ERROR"
                break
        n+=1
    if len(s)<y:
        g="ERROR"
    # print(s)
    print(g if g == "ERROR" else f"VALID {r}")
main()
