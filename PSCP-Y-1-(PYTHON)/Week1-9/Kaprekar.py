"""Kaprekar"""
def m_d(a,b,c,d):
    """mm"""
    if a < b:
        a, b = b, a
    if a < c:
        a, c = c, a
    if a < d:
        a, d = d, a
    if b < c:
        b, c = c, b
    if b < d:
        b, d = d, b
    if c < d:
        c, d = d, c
    return a,b,c,d
def mxmn(n):
    """Kaprekar"""
    s = 1
    n1 = 0
    n2 = 0
    n3 = 0
    n4 = 0
    for i in str(n):
        if s == 1:
            n1 = int(i)
        elif s == 2:
            n2 = int(i)
        elif s == 3:
            n3 = int(i)
        elif s == 4:
            n4 = int(i)
        s+=1
    m1,m2,m3,m4 = m_d(n1,n2,n3,n4)
    mx = int(str(m1)+str(m2)+str(m3)+str(m4))
    mn = int(str(m4)+str(m3)+str(m2)+str(m1))
    return mx,mn
def main():
    """Kaprekar"""
    o = 1
    numx,numn = mxmn(input())
    while numx-numn != 6174:
        k = numx-numn
        numx,numn = mxmn(k)
        o+=1
    print(o)
main()
