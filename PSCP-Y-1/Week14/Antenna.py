"""Antenna"""
import json
def main(r,l,s=0):
    """Antenna"""
    r=r*2+1
    l.sort()
    for i in l[:]:
        if i in l[:]:
            for j in l[:]:
                if j-i>=r-1:
                    s+=1
                    if j-i==r-1:
                        l.remove(j)
                    break
                if len(l[:])>1:
                    l.remove(j)
    if l:
        s+=1
    print(s)
main(int(input()),json.loads(input()))
