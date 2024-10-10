"""Kabata"""
def main():
    """Kabata"""
    t=[]
    for _ in range(int(input())):
        n = input()
        if "baka" in n:
            t.append("no")
            continue
        s=""
        o=0
        n=n.replace("bakka","baka")
        m=len(n)
        for i,j in zip(n,range(m)):
            if not j%2 and j:
                s+=" "
            s+=i
        s = s.split()
        for i in s:
            if not i in ("ba","ka","ta"):
                t.append("no")
                o=1
                break
        if not o:
            t.append("yes")
    for i in t:
        print(i)
main()
