"""Niwarn World"""
import math
def x(n):
    """x"""
    xl=2+((math.log(n**2,2))/((2*n)*(math.log(n,2))))
    return xl
def y(n,s):
    """y"""
    x1 = x(n)
    yl=(((0.5)+((2*s)**0.5))/(x1+3))
    return yl
def z(k):
    """z"""
    x1 = x(k)
    y1 = y(k,k)
    zl=(y1**2)+((8456*(x1**4))/(24*k))
    return zl
def main():
    """Niwarn World"""
    n = float(input())
    s = float(input())
    k = float(input())
    x1 = x(n)
    y1 = y(n,s)
    z1 = z(k)
    print(f"X: {x1:.1f}, Y: {y1:.1f}, Z: {z1:.1f}")
main()
