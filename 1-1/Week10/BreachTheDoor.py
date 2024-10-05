"""BreachTheDoor"""
def main():
    """BreachTheDoor"""
    text = input()
    text1=""
    for i in text:
        if i.isalpha() or i.isspace():
            text1+=i
    text1 = text1.split()
    for i in text1:
        if len(i)>6:
            print(i,end=" ")
main()
