"""Labs 07.01 - Insertion Sort"""
import json
def main(l,x):
    """Labs 07.01 - Insertion Sort"""
    l1=[l[0]]
    l.remove(l[0])
    count=0
    for _ in range(x):
        n=0
        for i in range(len(l1)-1,-1,-1):
            count+=1
            if l[0] > l1[i]:
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