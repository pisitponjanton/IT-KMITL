"""Kayak"""
def main():
    """Kayak"""
    num = int(input())
    n = input().split()
    l=[]
    m=len(n)
    n.sort(key= lambda x: int(x))
    for i,s in zip(n,range(m)):
        if i != n[-1]:
            l.append(int(n[s+1])-int(i))
    print(n)
    print(l)
    # for i in l:
main()
