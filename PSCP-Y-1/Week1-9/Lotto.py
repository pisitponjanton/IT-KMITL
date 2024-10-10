"""Lotto"""
def main():
    """Lotto"""
    h1 = input()
    h2 = input()
    h3 = input()
    h4 = input()
    h5 = input()
    h6 = input()
    h = input()
    n = 0
    if h == h1 :
        n+=6000000
    if h[4:6] == h2:
        n+=2000
    if h[0:3] == h3:
        n+=4000
    if h[0:3] == h4:
        n+=4000
    if h[3:6] == h5:
        n+=4000
    if h[3:6] == h6:
        n+=4000
    if h1 == "999999":
        if h in ("000000","999998"):
            n+=100000
    elif h1 == "000000":
        if h in ("000001","999999"):
            n+=100000
    else:
        if int(h) in (int(h1)-1,int(h1)+1):
            n+=100000
    print(n)
main()
