"""Runner"""
def main():
    """Runner"""
    d = float(input())
    n = int(input())
    l=[]
    t=[]
    t1=[]
    for _ in range(n):
        num = input().split()
        l.append(str((d-int(num[1]))/(int(num[0])))+" "+num[0])
    for i in l:
        t.append(str(i).split())
    for i, row in enumerate(t):
        for j, value in enumerate(row):
            t[i][j] = float(value)
    # print(t)
    for i, row in enumerate(t):
        t1.append(row[0])
    # print(t1)
    if t1.count(min(t1)) <= 1:
        print(t1.index(min(t1))+1)
    else:
        print(t1.index(min(t1))+2)
main()
