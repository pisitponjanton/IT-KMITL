"""ISBN"""
def main(n):
    """ISBN"""
    l=-sum(int(i)*j for i,j in zip(n,range(10,1,-1)))%11
    l = l if l<10 else "X"
    print(f"No {l}"if str(l)!=n[-1] else "Yes")
main(input().replace("-",""))
