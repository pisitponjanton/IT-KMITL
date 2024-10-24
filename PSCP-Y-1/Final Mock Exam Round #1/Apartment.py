"""Apartment"""
import math
def main(a,b,c,d,e):
    """Apartment"""
    if a<15:
        x=math.ceil((b-d*c)/(2*d))
        z=math.ceil((c*e-b)/(2*e))
    else:
        x=round((b-d*c)/(2*d))
        z=round((c*e-b)/(2*e))
    x=0 if x<=0 else a-c if x>=a-c else x
    z=0 if z<=0 else c-1 if z>=c-1 else z
    l=[[(b-d*x)*(c+x),c+x],[(b+z*e)*(c-z),c-z]]
    l.sort(key=lambda x: (-x[0],x[1]))
    print(f"{l[0][0]}\n{l[0][1]}")
main(int(input()),int(input()),int(input()),int(input()),int(input()))
