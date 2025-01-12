"""Water"""
def main(n,a,b,c,d):
    """Water"""
    s=0
    for _ in range(n):
        num=float(input())
        t=a*num
        if num>b:
            t=(b * a)+(num-b)*c
        if t<=d:
            t=0
        s+=t
    print(f"{s:.2f}")
main(int(input()),float(input()),float(input())
    ,float(input()),float(input()))
