"""Diginity"""
def main():
    """Diginity"""
    num = 1
    m=[]
    while int(num) > 0:
        num = input()
        num2 = num
        num1 = num
        while len(num2) > 1:
            num1 = 0
            for i in num2:
                num1 += int(i)
            num2 = str(num1)
        m.append(num1)
    m.pop()
    for i in m:
        print(i)
main()
