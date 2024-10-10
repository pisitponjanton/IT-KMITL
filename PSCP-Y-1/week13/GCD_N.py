"""GCD_N"""
def main():
    """GCD_N"""
    l=[]
    for _ in range(int(input())):
        l.append(int(input()))
    for i in range(min(l),0,-1):
        s=0
        for j in l:
            if not j%i:
                s+=1
        if s==len(l):
            print(i)
            break
main()
