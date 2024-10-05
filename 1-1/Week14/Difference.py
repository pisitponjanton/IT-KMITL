"""Difference"""
import json
def main(a,b,t=0):
    """Difference"""
    a.sort()
    b.sort()
    da = {i: list(a).count(i) for i in a}
    db = {i: list(b).count(i) for i in b}
    for (i,j),(_,j1) in zip(da.items(),db.items()):
        if abs(j-j1):
            t=1
            print(i,abs(j-j1))
    if not t:
        print("ONAJI DAYO!")
main(json.loads(input()),json.loads(input()))
