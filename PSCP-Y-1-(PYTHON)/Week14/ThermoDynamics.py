"""ThermoDynamics"""
import json
def num(n,s,r):
    """"num"""
    for i,j in enumerate(n[:]):
        if i<len(n)-1:
            if abs(j-n[i+1])>=2:
                r=1
                s+=1
                if n[i+1]>j:
                    n[i+1]-=1
                    n[i]+=1
                else:
                    n[i+1]+=1
                    n[i]-=1
                break
    return n,s,r
def numm(n,s):
    """numm"""
    o=0
    for i,_ in enumerate(n):
        for j,_ in enumerate(n):
            if abs(n[i]-n[j])>=2:
                s+=1
                o=1
                if n[i]>n[j]:
                    n[i]-=1
                    n[j]+=1
                else:
                    n[i]+=1
                    n[j]-=1
                break
        if o:
            break
    return n,s
def main(n,s=0):
    """ThermoDynamics"""
    n.sort()
    while max(n)-min(n)>=2:
        r=0
        n,s,r = num(n,s,r)
        if not r:
            n,s = numm(n,s)
    print(s)
main(json.loads(input()))
