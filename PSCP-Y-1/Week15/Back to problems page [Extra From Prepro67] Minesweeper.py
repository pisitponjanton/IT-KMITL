"""Back to problems page [Extra From Prepro67] Minesweeper"""
def nu(i1,j1,l,e,r=0):
    """Back to problems page [Extra From Prepro67] Minesweeper"""
    if i1-1>=0:
        for c,j in enumerate(l[i1-1]):
            r+=1 if j=="*" and c in (j1-1,j1,j1+1) else 0
    for c,j in enumerate(l[i1]):
        r+=1 if j=="*" and c in (j1-1,j1,j1+1) else 0
    if i1+1<=e:
        for c,j in enumerate(l[i1+1]):
            r+=1 if j=="*" and c in (j1-1,j1,j1+1) else 0
    return r
def main(n):
    """Back to problems page [Extra From Prepro67] Minesweeper"""
    l=[]
    for _ in range(int(n[2])):
        l.append(input().split())
    for i1,i in enumerate(l):
        s=[]
        for j1,j in enumerate(i):
            if j == "0":
                s.append(nu(i1,j1,l,int(n[2])-1))
            else:
                s.append(j)
        l[i1]=s
    for i in l:
        print(*i)
main(input().split())
