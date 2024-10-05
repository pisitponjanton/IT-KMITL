"""[Final 2019] Hamming"""
def main(n,m,s=0):
    """[Final 2019] Hamming"""
    for i,j in zip(n,m):
        if i!=j:
            s+=1
    print(s)
main(input(),input())
