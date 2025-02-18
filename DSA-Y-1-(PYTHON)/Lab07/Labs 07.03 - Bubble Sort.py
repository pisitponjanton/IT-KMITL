"""Labs 07.03 - Bubble Sort"""
import json
def main(l,x):
    """Labs 07.03 - Bubble Sort"""
    count,n=0,0
    while True:
        b = [True]
        for i in range(x,n,-1):
            if l[i]<l[i-1]:
                l[i],l[i-1]=l[i-1],l[i]
                b.append(False)
            count+=1
        print(l)
        n+=1
        if all(b):
            break
    print("Comparison times:",count)
main(json.loads(input()),int(input()))