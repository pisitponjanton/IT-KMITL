"""Sort"""
def main():
    """Sort"""
    l=[]
    while True:
        n=input()
        if n=="END":
            break
        l.append(int(n))
    for i1,_ in enumerate(l[:]):
        for j1,_ in enumerate(l[:]):
            if l[j1]>l[i1]:
                l[j1],l[i1]=l[i1],l[j1]
    for i in l:
        print(i)
main()
