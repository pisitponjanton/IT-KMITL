"""CaesarV1"""
def main():
    """CaesarV1"""
    n = int(input())
    t = input()
    s=""
    if n >= 26:
        n-=26
    if n <= -26:
        n+=26
    for i in t:
        if i.isalpha():
            if i.islower():
                y=ord(i)+n
                y-=26 if y>122 else 0
                y+=26 if y<97 else 0
                s+=chr(y)
            else:
                y=ord(i)+n
                y-=26 if y>90 else 0
                y+=26 if y<65 else 0
                s+=chr(y)
        else:
            s+=i
    print(s)
main()
