def main():
    """Fwdwd"""
    num = int(input("Input num: "))
    n=1
    while n<=num:
        if not n%15:
            print("FizzBuzz")
        elif not n%5:
            print("Buzz")
        elif not n%3:
            print("Fizz")
        else:
            print(n)
        n+=1
main()
