"""Exercise Recursive 2 - Flatten"""
import json
def flatten(n):
    """flatten"""
    l=[]
    for i in n:
        if isinstance(i,list):
            l += flatten(i)
        else:
            l.append(i)
    return l
def main(x,l=[]):
    """main"""
    for i in x:
        if isinstance(i,list):
            l+=flatten(i)
        else:
            l.append(i)
    l.sort(key=lambda x: -x)
    print(l)
main(json.loads(input()))