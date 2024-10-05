"""Bad Keyboard"""
def main():
    """Bad Keyboard"""
    t = input()
    t1=""
    for i in t:
        if i=="i":
            t1+="o"
        elif i=="o":
            t1+="i"
        elif i=="I":
            t1+="O"
        elif i=="O":
            t1+="I"
        else:
            t1+=i
    print(t1)
main()
