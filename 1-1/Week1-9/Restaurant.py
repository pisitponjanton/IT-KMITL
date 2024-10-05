"""Restaurant"""
def main():
    """Restaurant"""
    a = float(input())
    b = float(input())
    c = float(input())
    d = float(input())
    num1 = (a+d)*((100-c)/100)
    num2 = num1 - a
    if d > 0 and c >0:
        if a == b :
            num3 = a*(100-c)/100
            if num3 - num1 > 0:
                print(f"Yes {abs(num3-num1):.3f}")
            elif not num3 -num1:
                print("Yes")
            elif num3 - num1 < 0:
                print(f"No {abs(num3-num1):.3f}")
        elif not num2 or c == 100 or a+d < b:
            print("Yes")
        elif num2 > 0:
            print(f"No {abs(num2):.3f}")
        else:
            print(f"Yes {abs(num2):.3f}")
    else:
        print("Yes")
main()
