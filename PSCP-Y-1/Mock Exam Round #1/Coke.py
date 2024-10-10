"""Coke"""
def main():
    """Coke"""
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    if not b:
        print(a*d)
    else:
        n = d//b
        if not d%b:
            n-=1
        h = d-n
        print(0 if not d else h*a+n*c)
main()
