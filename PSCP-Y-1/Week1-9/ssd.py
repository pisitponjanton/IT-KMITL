"""rt"""
def main():
    """t"""
    num1 = int(input())
    if num1 < 10:
        print(1)
    else:
        i = 2
        n = 2
        while True:
            if num1 - 10*i < 0:
                print(n)
                break
            n+=1
            i+=1
main()
