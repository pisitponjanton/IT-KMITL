"""Counting Stars"""
def main():
    """Counting Stars"""
    n = input()
    s = ""
    d1=0
    d2=0
    d3=0
    n1=1
    for i in n:
        if not i.isspace():
            s+=i
            break
    for i in n[1:] :
        if i.isspace():
            s=""
        else:
            s+=i
        if s in ("~*","*~"):
            d1+=1
            s=""
        elif s == "*/":
            d2+=1
            s=""
        elif s == "**":
            d3+=1
            s=""
        if len(s) >= 2:
            s=s[1:]
        n1+=1
    if d1>0 or d2>0 or d3>0:
        print(f"constellation: {d3}\ncomet: {d1}\nshooting star: {d2}")
    else:
        print("Tonight is a quiet night.")
main()
