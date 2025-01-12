"""Solar System"""
def h(ind,n):
    """so hot🥵"""
    s,c='',0
    for i in n:
        if i==",":
            c+=1
        if c==ind-2:
            s+=i
        if c==ind:
            s+=i
    return s.replace(","," ")
def co(a,ind,n,center):
    """so cool😎"""
    s,c='',0
    for i in n:
        if i==",":
            c+=1
        if ind>center:
            if i==",":
                break
            s+=i
        elif ind<center:
            if c==a-1 and i!=",":
                s+=i
        else:
            if c in (0,a-1):
                s+=i
    return s.replace(","," ")
def main(n):
    """Solar System"""
    s,ind='',0
    a=sum(1 for i in n if i==",")
    center=(a+1)/2
    for i in n:
        s+=i
        if s=="Sun,":
            ind+=1
            break
        if i==",":
            ind+=1
            s=""
    print(f"Hot: {h(ind,n).strip()}")
    print(f"Cool: {co(a,ind,n,center).strip()}")
main((input()+" ").replace(" ",","))
