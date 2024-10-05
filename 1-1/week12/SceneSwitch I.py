"""SceneSwitch I"""
def main():
    """SceneSwitch I"""
    r=0
    l1,l2=[],[]
    while True:
        r+=1
        n = input()
        if n=="End":
            break
        n=float(n)
        if n>0:
            if r%2:
                l1.append(n)
            else:
                l2.append(n)
    s,t=0,1
    for i,j in zip(l1,l2):
        if abs(j-i)<=6 and t:
            s+=1
            t=0
        else:
            t=1
    print(s)
main()
