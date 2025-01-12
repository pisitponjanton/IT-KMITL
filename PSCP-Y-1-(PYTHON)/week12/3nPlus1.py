"""3nPlus1"""
def main():
    """22"""
    l=[]
    while True:
        n = int(input())
        if not n:
            break
        s=0
        while n!=1:
            s+=1
            if not n%2:
                n/=2
            else:
                n=n*3+1
        l.append(s+1)
    for i in l:
        print(i)
main()
