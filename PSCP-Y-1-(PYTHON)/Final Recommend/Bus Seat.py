"""Bus Seat"""
def main(a,b,n):
    """Bus Seat"""
    s,ss=a,a
    for j in range(1,a+1):
        ss=s
        for _ in range(b):
            print(f"{ss:02d}" if ss!=n else "XX",end=" ")
            ss+=a
        print()
        if not j%2 and j<a:
            print()
        s-=1
main(int(input()),int(input()),int(input()))
