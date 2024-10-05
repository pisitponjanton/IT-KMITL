"""Books"""
import math
def books1():
    """Books"""
    n = int(input())
    k = int(input())
    x = int(input())
    y = int(input())
    d = 0
    i = 0
    while n >= 1 :
        p = math.ceil(((x+i)/(y+i))*k)
        if p>=k:
            i+=n
            break
        d+=p
        i+=1
        if d>=k:
            d=0
            n-=1
    print(i)
books1()
