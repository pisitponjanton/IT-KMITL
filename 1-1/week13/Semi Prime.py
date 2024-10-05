"""Semi Prime"""
def main(n):
    """Semi Prime"""
    l,l1=[],[]
    r,s=0,0
    for j in range(2,n+1):
        t=1
        for i in range(2,int(j**0.5)+1):
            if not j%i:
                t=0
        if t :
            l.append(j)
    for i in l:
        if r<len(l):
            for j in l[r:]:
                if i*j<=n:
                    l1.append(i*j)
        r+=1
    for i in l1:
        if i <= n:
            s+=1
    print(s)
main(int(input()))
