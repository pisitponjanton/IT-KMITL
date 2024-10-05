"""B - Fully pair?"""
def main():
    """B - Fully pair?"""
    t = input()
    tt = t
    t1=""
    t2=""
    n=0
    for i in t:
        for j in tt:
            if i==j:
                t1+=j
        if len(t1)%2:
            t2+=i
        t1=""
        for j in tt:
            if not n:
                tt=""
            if j!=i:
                tt+=j
            n+=1
        n=0
    print(t2 if len(t2)>0 else "fully paired")
main()
