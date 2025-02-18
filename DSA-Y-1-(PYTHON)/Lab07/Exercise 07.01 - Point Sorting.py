"""Exercise 07.01 - Point Sorting"""
def f(l1,l2):
    l1 = l1.split()
    l2 = l2.split()
    if int(l1[0])+int(l1[1]) == int(l2[0])+int(l2[1]):
        return int(l1[1])>int(l2[1])
    else:
        return int(l1[0])+int(l1[1]) < int(l2[0])+int(l2[1])
def sorbb(l):
    n=0
    while True:
        b = [True]
        for i in range(len(l)-1,n,-1):
            if f(l[i],l[i-1]):
                l[i],l[i-1]=l[i-1],l[i]
                b.append(False)
        n+=1
        if all(b):
            break
    return l
def main():
    """Exercise 07.01 - Point Sorting"""
    for _ in range(int(input())):
        l=[]
        for _ in range(int(input())):
            l.append(input())
        l = sorbb(l)
        for i in l:
            print(i)
main()