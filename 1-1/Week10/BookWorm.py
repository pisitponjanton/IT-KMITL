"""BookWorm"""
def main():
    """BookWorm"""
    n = int(input())
    l = []
    for _ in range(n):
        allt = float(input())
        nbook = int(input())
        s=[]
        s1=0
        s2=0
        for i in range(nbook):
            s.append(float(input()))
        s.sort()
        for i in s:
            if s1+i<=allt:
                s1+=i
                s2+=1
        l.append(s2)
    for i in l:
        print(i)
main()
