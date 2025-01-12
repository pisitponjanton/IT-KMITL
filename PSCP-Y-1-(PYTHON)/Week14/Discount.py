"""Discount"""
def main(s=0):
    """Discount"""
    l=[]
    while True:
        n = input()
        if n == "ENTER":
            break
        l.append(int(n))
        s+=1
    l.sort()
    if s<=5:
        t=0
    elif 6<=s<12:
        t=1
    elif 12<=s<20:
        t=2
    elif 20<=s<25:
        t=4
    else:
        t=s//5
    t = sum(j for _,j in zip(range(t),l))
    print(sum(l)-t)
main()
