"""[Final 2021] Poisonous Vegetables"""
import json
def main(n,a,d):
    """[Final 2021] Poisonous Vegetables"""
    l=[]
    for _ in range(int(n[0])):
        num=json.loads("["+input().replace(" ", ",").replace("][", "],[")+"]")
        for i in num:
            if i[1]>a:
                l.append("[ - ]")
            elif i[0]==i[2]:
                l.append("[ o ]")
            else:
                l.append("[ x ]")
    for j,i in enumerate(l):
        print(i,end="")
        if not(j+1)%int(n[1]):
            d+=1
            print()
main(input().split(" x "),int(input()),int(input()))
