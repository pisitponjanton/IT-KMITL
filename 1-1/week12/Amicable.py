"""Amicable"""
def h(i):
    """Amicable"""
    s=0
    for j in range(1,int(i**0.5)+1):
        if not i%j:
            s+=j
            if j>1:
                s+=i//j
    return s
def main():
    """Amicable"""
    n = int(input())
    l=0
    for i in range(220,n+1):
        s=h(i)
        if s>i:
            s1=h(s)
            if s1==i:
                l+=s1+s
    print(l)
main()
