"""[Final 2021] SuperMarketV2"""
def main(n,a,b,c):
    """[Final 2021] SuperMarketV2"""
    l=[int(input()) for _ in range(n)]
    p=sum(l)
    l1=[(i*c)/100 for i in l]
    s1=[p]
    s2=s3=[p-i for i in l1]
    if p>=a:
        s3=[i*(100-b)/100 for i in s3]
    print(int(min(s1+s2+s3)))
main(int(input()),int(input()),int(input()),int(input()))
