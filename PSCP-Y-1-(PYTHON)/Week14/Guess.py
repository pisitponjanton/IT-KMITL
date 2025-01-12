"""Guess"""
def mn(s,n):
    """Guess"""
    if n[0] == ">" and n[2] == "YES":
        for i in range(min(s),int(n[1])+1):
            s.remove(i)
    elif n[0] == ">" and n[2] == "NO":
        for i in range(int(n[1])+1,max(s)+1):
            s.remove(i)
    elif n[0] == "<" and n[2] == "YES":
        for i in range(int(n[1]),max(s)+1):
            s.remove(i)
    elif n[0] == "<" and n[2] == "NO":
        for i in range(min(s),int(n[1])):
            s.remove(i)
    elif n[0] == "=" and n[2] == "YES":
        s=[int(n[1])]
    else:
        if int(n[1]) in s:
            s.remove(int(n[1]))
    return s
def main():
    """Guess"""
    s = list(range(101))
    while True:
        n = input().split()
        if "END" in n:
            break
        s=mn(s,n)
    print(*s)
main()
