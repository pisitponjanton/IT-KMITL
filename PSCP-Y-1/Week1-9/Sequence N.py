"""Sequence N"""
def main():
    """Sequence N"""
    num1 = int(input())
    num2 = " "
    for z in range(1,num1+1):
        for i in range(1,num1+1):
            num2 = " "
            if i in (1,num1):
                num2 = "*"
            if i == z and (not i in (1,num1)):
                num2 = "*"
            print(num2,end='')
        print()
main()
