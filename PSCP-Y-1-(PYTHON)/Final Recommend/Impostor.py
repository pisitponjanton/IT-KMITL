"""Impostor"""
import json
def main():
    """Impostor"""
    d,dd,s={},[],0
    while True:
        n=input()
        if n=="Start":
            s=1
        if n=="End":
            break
        if not s:
            d.update(json.loads(n))
        else:
            dd.append(n)
    im=sum(1 for j,i in d.items() if i=="Impostor" and j not in dd)
    print(f"{im} Impostor Remains\n***Alive***")
    d=sorted(d.items())
    for i,j in d:
        if i not in dd:
            print(f"{i} : {j}")
    print("***Dead***")
    for i,j in d:
        if i in dd:
            print(f"{i} : {j}")
main()
