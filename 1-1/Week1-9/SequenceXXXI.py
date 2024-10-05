"""SequenceXXX"""
def main():
    """SequenceXXX"""
    n1 = int(input())
    n2 = int(input())
    r=1
    z1=0
    z2=n1+1
    z3=n1-1
    for z in range(n1):
        w=1
        w1=0
        r=1
        for i in range(1,n1*n2 + n2):
            if not i%(n1+1) :
                print(" ",end='')
            else:
                if i == w or z in (0,n1-1):
                    print("*",end='')
                    if not r%2:
                        w+=2
                    else:
                        w+=n1-1
                    r+=1
                elif w1 in (z1,z1+z2,z1+z2*2):
                    print("*",end='')
                elif w1 in (z1+z2*3,z1+z2*4):
                    print("*",end='')
                elif w1 in (z1+z2*5,z1+z2*6,z3,z3+z2):
                    print("*",end='')
                elif w1 in (z3+z2*2,z3+z2*3,z3+z2*4,z3+z2*5,z3+z2*6):
                    print("*",end='')
                else:
                    print(" ",end='')
            w1+=1
        z1+=1
        z3-=1
        print()
main()
