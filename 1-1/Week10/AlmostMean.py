"""AlmostMean"""
def main():
    """AlmostMean"""
    n = int(input())
    l = []
    for _ in range(n):
        num = input().split()
        l.append(num)
    num=0
    t = []
    for i in range(n):
        num+=float(l[i][1])
        t.append(float(l[i][1]))
    num/=n
    t.append(num)
    t.sort()
    u=0
    for i in t:
        if i == num:
            break
        u+=1
    for i in range(n):
        if l[i][1] == str(t[u-1]):
            print(l[i][0]+"\t"+str(t[u-1]))
main()
