"""[Final 2021] Dancing"""
def ff(t,m,n):
    """[Final 2021] Dancing"""
    if t=="north":
        m-=n if not m in list(range(1,n+1)) else 0
    elif t=="northwest":
        m-=n if m in list(range(1,n**2+1,n)) and m!=1 \
        else 1 if m in list(range(2,n+1)) else (n+1) if m!=1 else 0
    elif t=="northeast":
        m-=n if m in list(range(n,n**2+1,n)) and m!=n \
        else -1 if m in list(range(1,n)) else (n-1) if m!=n else 0
    elif t=="west":
        m-=1 if m not in list(range(1,n**2+1,n)) else 0
    elif t=="east":
        m+=1 if m not in list(range(n,n**2+1,n)) else 0
    elif t=="southwest":
        m+=n if m in list(range(1,n**2+1,n)) and m!=n**2-(n-1) \
        else -1 if m in list(range(n**2-(n-2),n**2+1)) else (n-1) if m!=n**2-(n-1) else 0
    elif t=="south":
        m+=n if not m in list(range(n**2-(n-1),n**2+1)) else 0
    elif t=="southeast":
        m+=n if m in range(n,n**2+1,n) and m!=n**2 \
        else 1 if m in list(range(n**2-(n-1),n**2)) else (n+1) if m!=n**2 else 0
    return m
def main(n,x,r,s=0):
    """[Final 2021] Dancing"""
    m=((n**2)+1)//2
    e=1
    while True:
        t = input().lower().strip()
        if t in "ultimately":
            e=r if m==x else 1
            s+=5*e
            break
        if "dance" in t:
            e=r if m==x else 1
            s+=e
        else:
            m = ff(t,m,n)
            if m == x:
                e=r
            else:
                e=1
    print(f"Total point : {s}")
main(int(input()),int(input()),int(input()))
