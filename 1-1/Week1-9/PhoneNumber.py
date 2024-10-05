"""PhoneNumber"""
def main():
    """PhoneNumber"""
    num = input()
    t = input()
    n = 1
    num1 = ''
    if t == "Domestic":
        for i in num[::-1]:
            if not n%4:
                i = i+" "
            num1+= i
            n+=1
        print(num1[::-1])
    elif t == "International":
        for i in num[::-1]:
            if not n%4:
                i = i+" "
            num1+= i
            n+=1
        num1 = num1[:-1]
        print("+66"+num1[::-1])
main()
