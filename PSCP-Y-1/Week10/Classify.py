"""Classify"""
def main():
    """Classify"""
    l=[]
    l1=[]
    l2=[]
    l3=[]
    c=[]
    while True:
        num = input()
        if num == "END":
            break
        l2.append(num[:4])
    l2.sort()
    for i in l2:
        if not i in l3:
            c.append(l2.count(i))
            l1.append(i)
        l3.append(i)
    n = l1[0][:2]
    g=0
    j=0
    for i in l1:
        if i[:2] == n and not g:
            g=1
            l.append(i[:2]+" "+str(int(i[2:]))+" "+str(c[j]))
        elif i[:2] == n:
            l.append("--"+" "+str(int(i[2:]))+" "+str(c[j]))
        else:
            n=i[:2]
            l.append(i[:2]+" "+str(int(i[2:]))+" "+str(c[j]))
        j+=1
    for i in l:
        print(i)
main()
