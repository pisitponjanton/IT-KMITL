"""RockPaperScissor"""
def main():
    """RockPaperScissor"""
    n = input()
    a = 0
    b = 0
    for i in range(0,len(n),2):
        if n[i:i+2] in ("PR","SP","RS"):
            a+=1
        elif n[i:i+2] in ("RP","PS","SR"):
            b+=1
    if a>b :
        print(f"A win {a}-{b}")
    elif a<b :
        print(f"B win {b}-{a}")
    else:
        print(f"DRAW {b}")
main()
