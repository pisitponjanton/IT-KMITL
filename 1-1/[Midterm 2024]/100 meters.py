"""100 meters"""
def nit1(n1,n2,n3,n4,n5,n6,n7,n8):
    """feof"""
    s1=0
    n=10000000000000
    if n1<n:
        n=n1
        s1=1
    if n2<n:
        n=n2
        s1=2
    if n3<n:
        n=n3
        s1=3
    if n4<n:
        n=n4
        s1=4
    if n5<n:
        n=n5
        s1=5
    if n6<n:
        n=n6
        s1=6
    if n7<n:
        n=n7
        s1=7
    if n8<n:
        n=n8
        s1=8
    return s1,n
def nit2(n1,n2,n3,n4,n5,n6,n7,n8,n):
    """feof"""
    s2=0
    nn=10000000000000
    if n1<nn and n1!=n:
        nn=n1
        s2=1
    if n2<nn and n2!=n:
        nn=n2
        s2=2
    if n3<nn and n3!=n:
        nn=n3
        s2=3
    if n4<nn and n4!=n:
        nn=n4
        s2=4
    if n5<nn and n5!=n:
        nn=n5
        s2=5
    if n6<nn and n6!=n:
        nn=n6
        s2=6
    if n7<nn and n7!=n:
        nn=n7
        s2=7
    if n8<nn and n8!=n:
        nn=n8
        s2=8
    return s2,nn
def nit3(n1,n2,n3,n4,n5,n6,n7,n8,n,nn):
    """efef"""
    s3=0
    nnn=10000000000000
    if n1<nnn and n1!=n and n1!=nn:
        nnn=n1
        s3=1
    if n2<nnn and n2!=n and n2!=nn:
        nnn=n2
        s3=2
    if n3<nnn and n3!=n and n3!=nn:
        nnn=n3
        s3=3
    if n4<nnn and n4!=n and n4!=nn:
        nnn=n4
        s3=4
    if n5<nnn and n5!=n and n5!=nn:
        nnn=n5
        s3=5
    if n6<nnn and n6!=n and n6!=nn:
        nnn=n6
        s3=6
    if n7<nnn and n7!=n and n7!=nn:
        nnn=n7
        s3=7
    if n8<nnn and n8!=n and n8!=nn:
        nnn=n8
        s3=8
    return s3
def main():
    """100 meters"""
    n1 = float(input())
    n2 = float(input())
    n3 = float(input())
    n4 = float(input())
    n5 = float(input())
    n6 = float(input())
    n7 = float(input())
    n8 = float(input())
    s1,n = nit1(n1,n2,n3,n4,n5,n6,n7,n8)
    s2,nn = nit2(n1,n2,n3,n4,n5,n6,n7,n8,n)
    s3 = nit3(n1,n2,n3,n4,n5,n6,n7,n8,n,nn)
    print(s1,s2,s3)
main()
