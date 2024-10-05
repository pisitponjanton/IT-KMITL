"""VerticalHistogram"""
def h():
    """maxnumber"""
    n=input()
    l=[]
    m=[]
    m2=[]
    for i in n:
        if i.isalpha():
            l.append([i,n.count(i)])
    for i in l:
        m.append(i[1])
        m2.append(i)
    m1 = max(m)
    m=[]
    for i in range(1,m1+1):
        m.append(i)
    return m,m2
def main():
    """VerticalHistogram"""
    m=[]
    s=[]
    n1,n2 = h()
    n1.sort(reverse=True)
    n2.sort()
    for i in n1:
        if not i in m:
            m.append(i)
    for i in n2:
        if not i in s:
            s.append(i)
    for i in m:
        if i<10:
            print("",i,end="  ")
        else:
            print(i,end="  ")
        for j in s:
            if i <= j[1]:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
    print(' '*(3),end=" ")
    for i in s:
        print(i[0],end=' ')
main()
