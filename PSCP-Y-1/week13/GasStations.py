"""GasStations"""
def main(km,g,n):
    """GasStations"""
    l = [float(input()) for _ in range(n)]
    l1,r=l[0:1],0
    if not km in l:
        l.append(km)
    for i in l:
        if r<len(l)-1:
            r+=1
            l1.append(l[r]-i)
    t,s,u,r=0,0,0,0
    for i in l1:
        if not r and i==g:
            s+=1
        if r==len(l1)-1:
            break
        if i>g:
            u=1
            break
        if t+i>g:
            s+=1
            t=0
        t+=i
        r+=1
    print(s if not u else "depleted")
main(float(input()),float(input()),int(input()))
