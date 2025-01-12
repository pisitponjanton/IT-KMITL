"""[Final 2020] Train Station"""
def main(n1,n2,s=1,r=1):
    """[Final 2020] Train Station"""
    if not n1 or not n2:
        s=0
    for j,i in enumerate(n1):
        i=i.split(".")
        n1[j]=int(i[0])*60+int(i[1])
    for j,i in enumerate(n2):
        i=i.split(".")
        n2[j]=int(i[0])*60+int(i[1])
    n1.sort()
    n2.sort()
    for i,j in zip(n1[1:],n2[:-1]):
        if i<=j:
            t=0
            for z1,z in enumerate(n2[:r]):
                if i>z:
                    n2[z1]=1500
                    t=1
                    break
            if not t:
                s+=1
        r+=1
    print(s)
main(input().replace("[","").replace("]",'').replace(","," ").split(),
     input().replace("[","").replace("]",'').replace(","," ").split())
