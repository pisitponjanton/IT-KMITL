"""Milk"""
def main():
    """Milk"""
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    n1 = d//a
    n2 = n1
    if b > 0 and c:
        while n2 >= b:
            n2 = n2-b+c
            n1+=c
    print(n1)
main()
 