"""FORFBall"""
def main():
    """FORFBall"""
    n = input()
    a=1
    b=0
    c=0
    for i in n:
        if i == "A":
            if not a and not c:
                b=0
                a=1
            elif a and not c:
                a=0
                b=1
        if i == "B":
            if not b and not a:
                b=1
                c=0
            elif b and not a:
                b=0
                c=1
        if i == "C":
            if not c and not b:
                c=1
                a=0
            elif c and not b:
                c=0
                a=1
    print(1 if a==1 else 2 if b==1 else 3)
main()
