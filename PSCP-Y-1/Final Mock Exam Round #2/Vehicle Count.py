"""[Mock Final 2023] Vehicle Count"""
def main():
    """[Mock Final 2023] Vehicle Count"""
    s=[0]*5
    l,n=[],input()
    while True:
        n = input().replace("|","").replace("   ",' ').replace(" x ","x")
        if "-" in n:
            break
        if l:
            for j,i in enumerate(n):
                l[j]+=i
        else:
            l=[[i] for i in n]
    for i in l:
        r='|'
        for j in i:
            r+="".join(j)
        r+="|"
        r=r.split()
        for x in r:
            s[0]+=1 if "x" == x else 0
            s[1]+=1 if "xx" == x else 0
            s[2]+=1 if "xxx" == x else 0
            s[4]+=1 if x in ("|x","|xx","|xxx","x|","xx|","xxx|","|x|","|xx|","|xxx|") else 0
        s[3] += len([i1 for i1 in r if i1 not in \
        ('x','xx','xxx',"|x","|xx","|xxx","x|","xx|","xxx|","|","|x|","|xx|","|xxx|")])
    for i in s:
        print(i)
main()
