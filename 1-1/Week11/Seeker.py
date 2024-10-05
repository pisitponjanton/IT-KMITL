"""Seeker"""
def main():
    """Seeker"""
    n = input()
    l = []
    t=""
    num=0
    for i in n:
        if i.isnumeric():
            t+=i
        if not i.isnumeric() or i==n[-1]:
            if t:
                l.append(t)
            t=""
    for i in l:
        num+=int(i)
    print(num)
main()
