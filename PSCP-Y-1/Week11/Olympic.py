"""Olympic"""
def main():
    """Olympic"""
    n = [ input().split() for _ in range(int(input()))]
    nn = len(n)
    for i,j in zip(n,range(nn)):
        n[j].append(int(i[1])+int(i[2])+int(i[3]))
    n.sort(key=lambda x: (-int(x[1]),-int(x[2]),-int(x[3]),x[0][:]))
    l=0
    n2=[[]]
    o=0
    e=0
    for i,j in zip(n,n2):
        if i[1:] != j[2:]:
            l+=1
            if o:
                l+=e
                e=0
                o=0
        else:
            o=1
            e+=1
        n2.append([l]+i)
    n2.pop(0)
    for i in n2:
        print(i[0],i[1],i[2],i[3],i[4],i[5])
main()
