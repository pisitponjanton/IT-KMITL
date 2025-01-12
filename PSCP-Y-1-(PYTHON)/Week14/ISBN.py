"""ISBN"""
def main(n):
    """ISBN"""
    l = -sum(int(i)*j for i,j in zip(n[:-1],range(10,1,-1)))%11
    l="X" if l==10 else l
    if str(l) == n[-1]:
        print("Yes")
    else:
        print("No",l)
main(input().replace("-",""))
