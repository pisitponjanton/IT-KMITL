"""Labs 07.04 - Seats Number (Insertion Sorting)"""
import json
def ch(x,y):
    """x,y"""
    if x[0] == y[0]:
        return int(x[1:]) > int(y[1:])
    else:
        return ord(x[0]) > ord(y[0])
def main(l,x):
    """Labs 07.04 - Seats Number (Insertion Sorting)"""
    l1=[l[0]]
    l.remove(l[0])
    count=0
    for _ in range(x):
        n=0
        for i in range(len(l1)-1,-1,-1):
            count+=1
            if ch(l[0],l1[i]):
                l1.insert(i+1,l[0])
                l.remove(l[0])
                n=1
                break
        if not n:
            l1.insert(0,l[0])
            l.remove(l[0])
        print(l1+l)
    print("Comparison times:",count)
main(json.loads(input()),int(input()))