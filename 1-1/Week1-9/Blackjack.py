"""Blackjack"""
def npl2(x):
    """Blackjack"""
    if x > 9:
        t = 2+x
    else:
        t = 12+x
    return t
def pnum(x):
    """Blackjack"""
    if x in ("J","Q","K"):
        x = 10
    elif x == "A":
        x = 11
    else:
        x=int(x)
    return x
def numlist(x):
    """Blackjack"""
    if x[0]+x[1] >10:
        t = 1+x[0]+x[1]
    else:
        t = 11+x[0]+x[1]
    return t
def main():
    """Blackjack"""
    num = int(input())
    t=0
    pl = []
    q = 0
    j = []
    for _ in range(num):
        p = input()
        pl.append(p)
        p = pnum(p)
        t+=p
    npl = pl.count('A')
    if num == 2:
        if npl == 2:
            t = 12
    elif num == 3:
        for i in pl:
            if i != "A":
                if i in ("J","Q","K"):
                    q = 10
                    j.append(q)
                else:
                    q = int(i)
                    j.append(q)
        if npl == 1:
            t = numlist(j)
        elif npl == 2:
            t = npl2(q)
        elif npl == 3:
            t = 13
    print(t)
main()
