"""Taking Turns"""
import json
def main(x):
    """Taking Turns"""
    x1,l,r=[],0,-1
    for i,_ in enumerate(x):
        if not i%2 and i:
            l,r=r,l
        if not i%2:
            x1.append(x[r])
            r-=1 if r<0 else -1
        else:
            x1.append(x[l])
            l+=1 if l>=0 else -1
    print(x1)
main(json.loads(input()))
