"""SequenceXXX"""
def main():
    """SequenceXXX"""
    n1 = int(input())
    n2 = int(input())
    w=n1
    for _ in range(n2):
        for z in range(n1):
            for i in range(n1):
                if i in (0,n1-1) or z in (0,n1-1):
                    print("*",end='')
                elif z == i or i == w-1:
                    print("*",end='')
                else:
                    print(" ",end='')
            w-=1
            print()
        w=n1
main()
