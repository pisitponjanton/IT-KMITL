"""Labs 07.05 - Seats Number (Selection Sorting)"""
import json
def ch(x,y):
    """x,y"""
    if x[0] == y[0]:
        return int(x[1:]) <= int(y[1:])
    else:
        return ord(x[0]) <= ord(y[0])
def main(l,x):
    """Labs 07.05 - Seats Number (Selection Sorting)"""
    count=0
    for i in range(x):
        s=i
        for j in range(i+1,x+1):
            if ch(l[j],l[i]) and ch(l[j],l[s]):
                s = j
            count+=1
        l[i],l[s]= l[s],l[i]
        print(l)
    print("Comparison times:",count)
main(json.loads(input()),int(input()))