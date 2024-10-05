"""[Final 2019] Sort"""
def main():
    """[Final 2019] Sort"""
    l=[]
    while True:
        n=input()
        if n == "END":
            break
        if l:
            t = 0
            for i,j in zip(l,range(0,len(l))):
                if int(n)>i:
                    l.insert(j,int(n))
                    t=1
                    break
            if not t:
                l.append(int(n))
        else:
            l.append(int(n))
    for i in l[::-1]:
        print(i)
main()
