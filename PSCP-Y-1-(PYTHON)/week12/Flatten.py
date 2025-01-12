"""Flatten"""
import json
def lisst(x):
    """list"""
    l=[]
    for i in x:
        if isinstance(i,list):
            l=l+lisst(i)
        if isinstance(i,int):
            l.append(i)
    return l
def main(n):
    """Flatten"""
    n.sort(reverse=True)
    print(n)
main(lisst(json.loads(input())))
