"""Exercise 07.02 - Runner"""
def f(l1,l2,d):
    l1 = l1[1].split()
    l2 = l2[1].split()
    if (d-int(l1[1]))/int(l1[0]) == (d-int(l2[1]))/int(l2[0]):
        return int(l1[0])>int(l2[0])
    else:
        return (d-int(l1[1]))/int(l1[0]) < (d-int(l2[1]))/int(l2[0])
def sorbb(l,d):
    for i in range(len(l)-1,0,-1):
        if f(l[i],l[i-1],d):
            l[i],l[i-1]=l[i-1],l[i]
    return l
def main(d,n):
    """Exercise 07.02 - Runner"""
    l = []
    for i in range(1,n+1):
        l.append([i,input()])
    l = sorbb(l,d)
    print(l[0][0])
main(int(input()),int(input()))