"""Sequence XII"""
def main():
    """main"""
    num1 = int(input())
    n = 2*num1 - 1
    n1 = num1
    n2 = 2
    n3 = num1-1
    n4 = num1
    n5 = 2
    for z in range(1,n+1):
        if z in (1,n):
            for i in range(num1,0,-1):
                print(f"{i:0>2}",end=' ')
            for i in range(2,num1+1):
                print(f"{i:0>2}",end=' ')
        else:
            if 1<z<=num1:
                for i in range(n1,num1+1):
                    print(f"{i:0>2}",end=' ')
                for i in range(num1-1,z-1,-1):
                    print(f"{i:0>2}",end=' ')
                for i in range(z+1,num1+1):
                    print(f"{i:0>2}",end=' ')
                for i in range(num1-1,n1-1,-1):
                    print(f"{i:0>2}",end=' ')
            else:
                for i in range(n2,num1+1):
                    print(f"{i:0>2}",end=' ')
                n2+=1
                for i in range(num1-1,n3-1,-1):
                    print(f"{i:0>2}",end=' ')
                n3-=1
                for i in range(n4,num1+1):
                    print(f"{i:0>2}",end=' ')
                n4-=1
                for i in range(num1-1,n5-1,-1):
                    print(f"{i:0>2}",end=' ')
                n5+=1
        n1-=1
        print()
main()
