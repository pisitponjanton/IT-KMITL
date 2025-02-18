"""Labs 07.06 - Seats Number (Bubble Sorting)"""
import json
def ch(x,y):
    """x,y"""
    if x[0] == y[0]:
        return int(x[1:]) < int(y[1:])
    else:
        return ord(x[0]) < ord(y[0])
def main(l,x):
    """Labs 07.06 - Seats Number (Bubble Sorting)"""
    count,n=0,0
    while True:
        b = [True]
        for i in range(x,n,-1):
            if ch(l[i],l[i-1]):
                l[i],l[i-1]=l[i-1],l[i]
                b.append(False)
            count+=1
        print(l)
        n+=1
        if all(b):
            break
    print("Comparison times:",count)
main(json.loads(input()),int(input()))