"""Point Sorting"""
def main():
    """Point Sorting"""
    ll=[]
    t = int(input())
    for _ in range(t):
        l=[]
        n = int(input())
        for _ in range(n):
            num = input()
            num=num.split()
            l.append([int(num[0])+int(num[1])]+num)
        l.sort(key=lambda x: (int(x[0]), -int(x[2])))
        for i in l:
            ll.append(i[1]+" "+i[2])
    for i in ll:
        print(i)
main()
