"""Impostor"""
import json
def main():
    """Impostor"""
    d={}
    d1={}
    num=0
    while True:
        n = input()
        if n=="Start":
            while True:
                n = input()
                if n == "End":
                    break
                d1[n]=d[n]
                del d[n]
            break
        d.update(json.loads(n))
    for i in d.values():
        if i == "Impostor":
            num+=1
    d=sorted(d.items())
    d1=sorted(d1.items())
    print(num,"Impostor Remains")
    print("***Alive***")
    for i in d:
        print(i[0],":",i[1])
    print("***Dead***")
    for i in d1:
        print(i[0],":",i[1])
main()
