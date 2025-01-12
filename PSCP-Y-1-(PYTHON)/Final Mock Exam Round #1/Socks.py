"""Socks"""
def main(x):
    """Socks"""
    s=""
    for i in x:
        if not i in s:
            s+=i*(((x.count(i))//2)*2)
    s=list(s)
    s.sort()
    if s:
        for j,i in enumerate(s):
            if not (j+1)%2:
                print(i,end=' ')
            else:
                print(i,end='')
        print()
    else:
        print("None")
    print(len(s)//2)
main(input())
