"""Factors"""
def main():
    """Factors"""
    l=[]
    for _ in range(int(input())):
        d={}
        n=int(input())
        for i in range(2,n+1):
            if not n%i:
                d[i]=1
                n//=i
                while not n%i:
                    d[i]+=1
                    n//=i
        l.append(d.items())
    for i in l:
        l1=""
        r=0
        for i1,i2 in i:
            if r!=len(i)-1:
                if i2>1:
                    l1+=f"{i1}**{i2} x "
                else:
                    l1+=str(i1)+" x "
            else:
                if i2>1:
                    l1+=f"{i1}**{i2}"
                else:
                    l1+=str(i1)
            r+=1
        print(l1)
main()
