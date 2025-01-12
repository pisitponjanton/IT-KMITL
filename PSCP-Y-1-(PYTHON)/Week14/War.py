"""War"""
import json
def main(n1,n2):
    """War"""
    s=0
    n1.sort(reverse=True)
    n2.sort(reverse=True)
    for i in n1:
        if i<n2[-1]:
            break
        for j in n2[:]:
            if i>j:
                s+=i
                n2.remove(j)
                break
    print(s)
main(json.loads(input()),json.loads(input()))
