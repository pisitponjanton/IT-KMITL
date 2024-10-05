"""CuteCat CuteFox"""
def vv(x):
    """fefef"""
    t=""
    tt=""
    for i in x[1]:
        if str(i).isnumeric():
            t+=i
        else:
            tt+=i
    return tt,int(t)
def main():
    """CuteCat CuteFox"""
    d={}
    cat=0
    fox=0
    for _ in range(int(input())):
        n = input().replace("}","").replace("{","")
        n = n.split(" : ")
        k=n[0][1:-1]
        v=n[1][1:-1]
        d[k]=v
    if "Cat01" not in d.values() and "Garfield" not in d:
        k = "Garfield"
        v = "Cat01"
        d[k]=v
    if "Fox01" not in d.values() and "Fubuki" not in d:
        k = "Fubuki"
        v = "Fox01"
        d[k]=v
    for i in d.values():
        if i[:3]=="Cat":
            cat+=1
        else:
            fox+=1
    d = dict(sorted(d.items(), key=vv))
    print(f"Cat : {cat}\nFox : {fox}")
    for i,j in d.items():
        print(i,":",j)
main()
