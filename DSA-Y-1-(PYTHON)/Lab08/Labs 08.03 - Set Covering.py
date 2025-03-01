"""Labs 08.03 - Set Covering"""
import json
def main(l,x):
    """main"""
    l1 = []
    name_Covering = []
    boolean = False
    for _ in range(x):
        l1.append(json.loads(input()))
    for i in l1:
        for j in i["Cities"]:
            if j in l:
                boolean = True
    while boolean:
        l1.sort(key=lambda x: ( -len(x["Cities"]) , -len([i for i in x["Cities"] if i in l])))
        for i in l1[0]["Cities"]:
            if i in l[:]:
                l.remove(i)
                name_Covering.append(l1[0]["Name"])
        l1.remove(l1[0])
        if not l[:] or not l1:
            break
    
    name_Covering = list(set(name_Covering))
    name_Covering.sort()
    print(name_Covering)
main(json.loads(input()),int(input()))