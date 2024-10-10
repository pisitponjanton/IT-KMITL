"""Ticket Fare"""
def main():
    """Ticket Fare"""
    n = int(input())
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    f = int(input())
    g = int(input())
    num=0
    run = abs(g-f)
    if g<=n and f<=n:
        if run <= a:
            num+=b
        else:
            run-=a
            num+=b
            if run<c:
                num+=d*run
            else:
                run-=c
                num+=c*d
                num+=e*run
        print(num)
    else:
        print("Error")
main()
