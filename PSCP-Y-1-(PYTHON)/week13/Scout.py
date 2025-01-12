"""Scout"""
def main():
    """Scout"""
    for _ in range(int(input())):
        n1,egg  = input().split(), input().split()
        egg = [int(i) for i in egg]
        egg.sort(key=lambda x:x)
        p,q = int(n1[1]),int(n1[2])
        p1,q1=0,0
        for i in egg:
            if p1+1<=p and q1+int(i)<=q:
                p1+=1
                q1+=int(i)
        print(p1)
main()
