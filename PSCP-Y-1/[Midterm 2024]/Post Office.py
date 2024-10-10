"""Post Office"""
def nn(x):
    """Post Office"""
    n=0
    if 0<=x<=10:
        n+=16
    elif 10<x<=20:
        n+=18
    elif 20<x<=100:
        n+=23
    elif 100<x<=250:
        n+=28
    elif 250<x<=500:
        n+=33
    elif 500<x<=1000:
        n+=48
    elif 1000<x<=2000:
        n+=68
    return n+13
def mm(x):
    """Post Office"""
    m=0
    if 0<=x<=500:
        m+=45
    elif 500<x<=1000:
        m+=55
    elif 1000<x<=2000:
        m+=70
    return m+15
def main():
    """Post Office"""
    n = int(input())
    m = int(input())
    n1=0
    m1=0
    for _ in range(n):
        wn = float(input())
        n1+=nn(wn)
    for _ in range(m):
        wm = float(input())
        m1+=mm(wm)
    print(m1+n1)
main()
