"""Real"""
def ief(x):
    """Real"""
    t=""
    n=0
    if x[:7] == "1111110":
        t+="0"
    elif x[:7] == "0110000":
        t+="1"
    elif x[:7] == "1101101":
        t+="2"
    elif x[:7] == "1111001":
        t+="3"
    elif x[:7] == "0110011":
        t+="4"
    elif x[:7] == "1011011":
        t+="5"
    elif x[:7] == "1011111":
        t+="6"
    elif x[:7] == "1110000":
        t+="7"
    elif x[:7] == "1111111":
        t+="8"
    elif x[:7] == "1111011":
        t+="9"
    else:
        n=1
    if x[7] == "1":
        t+="."
    n = 1 if t == "." else n
    return t,n
def main():
    """Real"""
    t1 = ""
    n2=0
    for _ in range(3):
        n=""
        t2=""
        for _ in range(8):
            n1 = input()
            if n1 == "off":
                n+="0"
            else:
                n+="1"
        t2,n2=ief(n)
        if n2 :
            break
        t1+=t2
    if not n2 and t1.count(".") < 2:
        print(f"{float(t1):.2f}")
    else:
        print("Error")
main()
