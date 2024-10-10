"""US Interstate Number System"""
def main():
    """US Interstate Number System"""
    n = str(int(input()))
    if len(n)==2:
        n="0"+n
    elif len(n)==1:
        n="00"+n
    n1=""
    n2=""
    if int(n[0])>0 and int(n[2]) in (0,5) and n[1:]!="00":
        if not int(n[0])%2:
            n1= "Even"
        else:
            n1 = "Odd"
        n2 = "Minor"
    else:
        if int(n[2])==5:
            n1 = "Vertical"
        elif not int(n[2]) and int(n[1]):
            n1 = "Horizontal"
        n2 = "Major"
    if n1:
        print("" if not n1 else f"{n1} {n2} Interstate")
    print("Others" if not n1 else f"I-{int(n[1:])}")
main()
        