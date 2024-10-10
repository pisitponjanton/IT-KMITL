"""Parity"""
def main():
    """Parity"""
    num = input()
    eo = input()
    n=0
    for i in num:
        if i == "1":
            n+=1
    if not n%2:
        if eo == "Even":
            num=num+"0"
        else:
            num=num+"1"
    else:
        if eo == "Even":
            num=num+"1"
        else:
            num=num+"0"
    print(num)
main()
