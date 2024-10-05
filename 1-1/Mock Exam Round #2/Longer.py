"""Longer"""
import math
def mian():
    """Longer"""
    r = float(input())
    a = float(input())
    b = float(input())
    lr = 2*math.pi*r
    lab = 2*a+2*b
    if lr > lab:
        print("Circle is longer")
    elif lr < lab:
        print("Rectangle is longer")
    else:
        print("Equal")
    print(f"{abs(lr-lab):.5f}")
mian()
