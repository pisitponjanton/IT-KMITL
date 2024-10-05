"""Roman"""
def roman(i):
    """ROMAN"""
    num=0
    if i == "N":
        num+=90
    elif i == "L":
        num+=50
    elif i == "F":
        num+=40
    elif i == "X":
        num+=10
    elif i == "n":
        num+=9
    elif i == "V":
        num+=5
    elif i == "f":
        num+=4
    elif i == "I":
        num+=1
    return num
def main():
    """Roman"""
    n = input().replace("IV","f").replace("IX","n").replace("XL","F")
    n = n.replace("XC","N").replace("CD","R").replace("CM","G")
    num=0
    for i in n:
        if i == "M":
            num+=1000
        elif i == "G":
            num+=900
        elif i == "D":
            num+=500
        elif i == "R":
            num+=400
        elif i == "C":
            num+=100
        else:
            num+=roman(i)
    print(num)
main()
