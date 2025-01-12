"""Password"""
import math
def re(x):
    "dwdw"
    y=''
    if x<28:
        y="Very Weak"
    elif 28<=x<36:
        y="Weak"
    elif 36<=x<60:
        y="Reasonable"
    elif 60<=x<128:
        y="Strong"
    elif x>=128:
        y="Very Strong"
    return y
def main():
    """Password"""
    t = input()
    n1=0
    n2=0
    n3=0
    n4=0
    l=0
    for i in t:
        if i.isnumeric():
            n1=10
        elif i.isupper():
            n2=26
        elif i.islower():
            n3=26
        elif not i.isalnum():
            n4=32
        l+=1
    r = n1+n2+n3+n4
    e = math.log(r**l,2)
    print(int(e))
    print(re(e))
main()
