"""Solar System"""
def sunindx(n):
    """findindexsun"""
    s=0
    s1=0
    s2=0
    t=""
    for i in n:
        if not s:
            s=1
        if s:
            t+=i
            if t == "Sun,":
                s2=s1+1
            if i == ",":
                t=""
                s=0
                s1+=1
                continue
    return s1,s2
def fi(n,n1):
    """findhotandcool"""
    s=0
    s1=0
    t=""
    for i in n:
        if s1 == n1:
            s=1
        if s:
            t+=i
            if i == ",":
                break
        if i == ",":
            s1+=1
    return t
def solar():
    """Solar System"""
    hot = ""
    cool = ""
    n = (input()+" ").replace(" ",",")
    s1,sun = sunindx(n)
    if s1 == sun:
        hot= fi(n,sun-2)
        cool= fi(n,0)
    elif sun == 1:
        hot= fi(n,1)
        cool= fi(n,s1-1)
    elif not s1%2:
        hot1 = fi(n,sun-2)
        hot2 = fi(n,sun)
        if sun > (s1+1)//2 :
            cool = fi(n,0)
        else:
            cool = fi(n,s1-1)
        hot = hot1+" "+hot2
    elif s1%2:
        hot1 = fi(n,sun-2)
        hot2 = fi(n,sun)
        if sun == (s1+1)//2:
            cool1 = fi(n,0)
            cool2 = fi(n,s1-1)
            cool = cool1+" "+cool2
        elif sun < (s1+1)//2:
            cool = fi(n,s1-1)
        else:
            cool = fi(n,0)
        hot = hot1+" "+hot2
    print("Hot:",hot.replace(",","").strip())
    print("Cool:",cool.replace(",","").strip())
solar()
