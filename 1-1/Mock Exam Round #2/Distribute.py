"""Distribute"""
def main():
    """Distribute"""
    money = int(input())
    num = int(input())
    if num>money:
        print(-1)
    elif money-num<8:
        print(0)
    else:
        if money/num>8:
            print(num-1)
        else:
            n2=0
            n = money-num
            n2=n//7
            if n%7==3 and num-n2==1:
                n2-=1
            print(n2)
main()
