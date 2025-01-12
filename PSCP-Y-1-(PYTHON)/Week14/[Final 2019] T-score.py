"""[Final 2019] T-score"""
def main(n,m):
    """[Final 2019] T-score"""
    l = [int(input()) for _ in range(n)]
    sx,m = sum(l),m-1
    xb = sx/n
    sx2 = [i**2 for i in l]
    sd = ((n*sum(sx2) - sx**2)/(n*(n-1)))**0.5
    for i in l:
        z = (i-xb)/sd
        print(f"{50+(10*z):.2f}")
main(int(input()),int(input()))
