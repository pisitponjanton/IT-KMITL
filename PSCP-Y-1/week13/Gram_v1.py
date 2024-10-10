"""Gram_v1"""
def main():
    """Gram_v1"""
    n = list(input())
    l=[]
    d={}
    r=1
    for i in n:
        if r<len(n):
            l.append(i+n[r])
        r+=1
    for i in l:
        d[i]=l.count(i)
    for i,j in d.items():
        if j==max(d.values()):
            print(i)
            break
    print(max(d.values()))
main()
