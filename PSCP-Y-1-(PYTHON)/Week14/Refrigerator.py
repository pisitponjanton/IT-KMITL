"""Refrigerator"""
def main(n,c):
    """Refrigerator"""
    l,s=[0]*n,0
    for i,j in enumerate(c):
        l[i]+=int(j)
    while min(l):
        l.sort()
        for i in range(1,len(l)):
            l[i]-=1
        s+=1
    print(s)
main(int(input()),input().split())
