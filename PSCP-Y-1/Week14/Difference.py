"""Difference"""
import json
def main(a,b,t=0):
    """Difference"""
    se1 = list(set(a).difference(set(b)))+list(set(b).difference(set(a)))
    a = [(i,a.count(i)) for i in a]
    b = [(i,b.count(i)) for i in b]
    if se1:
        for i in se1:
            if not i in [j[0] for j in a]:
                a.append((i,0))
            if not i in [j[0] for j in b]:
                b.append((i,0))
    a=list(set(a))
    b=list(set(b))
    a.sort()
    b.sort()
    for i,j in zip(a,b):
        if abs(i[1]-j[1]):
            t=1
            print(i[0],abs(i[1]-j[1]))
    if not t:
        print("ONAJI DAYO!")
main(json.loads(input()),json.loads(input()))
