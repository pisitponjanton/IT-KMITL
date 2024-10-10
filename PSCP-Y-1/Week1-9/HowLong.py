"""HowLong"""
def main():
    """main"""
    num1 =int(input())
    n = 1
    if num1 >= 0:
        while True:
            if num1-10**n < 0:
                print(n)
                break
            n+=1
    else:
        while True:
            if abs(num1)-10**n < 0:
                print(n)
                break
            n+=1
main()
