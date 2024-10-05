"""Pringles"""
def pringles():
    """Pringles"""
    t = input()
    c = input()
    b = input()
    n = int(input())
    num = 0
    s = 0
    r = 0
    c1 = ''
    for i in c[:-1]:
        if s == n:
            break
        if i == ")":
            num+=1
        c1+=" "
        s+=1
    c1 = c1+c[s:]
    for i in c1:
        if i == ")":
            r+=1
    print(num)
    print("There are still some left." if r >= 1 else "None.")
    print(t)
    print(c1)
    print(b)
pringles()
