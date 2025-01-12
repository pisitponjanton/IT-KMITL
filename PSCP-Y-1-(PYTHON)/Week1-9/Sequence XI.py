"""t"""
def main():
    """t"""
    num1 = int(input())
    n = 2*num1 - 1
    n1 = 1
    n2 = n
    n3 = num1+1
    z1 = num1-1
    for z in range(1,n+1):
        if z <= num1:
            for i in range(1,n+1):
                print(f"{n1:0>2}",end=' ')
                if i >= n2:
                    n1-=1
                elif i < z:
                    n1+=1
            n1 = 1
            n2 -= 1
        elif z > num1:
            n1=1
            for i in range(1,n+1):
                print(f"{n1:0>2}",end=' ')
                if i >= n3:
                    n1-=1
                elif i < z1:
                    n1+=1
            z1-=1
            n1 = 1
            n3 += 1
        print()
main()
