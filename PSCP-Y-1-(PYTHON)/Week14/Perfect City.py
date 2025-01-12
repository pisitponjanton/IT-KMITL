"""Perfect City"""
def main(x,y,x1,y1):
    """Perfect City"""
    o = min((int(abs(x1)+1)-abs(x1))+(int(abs(x)+1)-abs(x))+abs(y1-y),
    abs(int(abs(x1))-abs(x1))+abs(int(abs(x))-abs(x))+abs(y1-y))
    print(f"{abs(x1-x)+abs(y1-y):.2f}" if y==y1 or (int(abs(x1-x)) and int(abs(y1-y)))\
    or (int(x)==x and int(abs(y1-y))) or (int(x1)==x1 and int(abs(y1-y))) or\
    (int(abs(y1-y)) and int(x)!=int(x1))\
    else f"{o:.2f}")
main(float(input()),float(input()),float(input()),float(input()))
