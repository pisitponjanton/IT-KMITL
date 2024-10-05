"""Diamond II"""
def main():
    """Diamond II"""
    m = int(input())
    n = int(input())
    l=[]
    o = [0]*n
    for _ in range(m):
        num1=[]
        num = input().split()
        for i in num:
            num1.append(int(i))
        l.append(num1)
    for j in range(2):
        for i in range(10):
            o[i]+=l[j][i]
    r = o.index(max(o))
main()
