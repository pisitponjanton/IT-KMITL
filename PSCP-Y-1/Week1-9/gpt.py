"""t"""
def main():
    """t"""
    num1 = int(input())
    n = num1-1
    if num1 != 1:
        for i in range(1,num1+n+1):
            print(f"{1:0>2}",end=' ')
        print()
        for z in range(1,num1+1+n-2):
            for i in range(1,num1+1):
                if i==num1 and z != num1-1:
                    i=num1-1
                print(f"{i:0>2}",end=' ')
            for j in range(num1-1,0,-1):
                print(f"{j:0>2}",end=' ')
            print()
        for i in range(1,num1+n+1):
            print(f"{1:0>2}",end=' ')
    else:
        for i in range(1,num1+n+1):
            print(f"{1:0>2}",end=' ')
    print()
main()
