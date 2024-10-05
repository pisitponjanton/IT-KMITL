"""Diamond I"""
def main():
    """Diamond I"""
    m = int(input())
    n = int(input())
    l=[0]*n
    for _ in range(m):
        j=0
        num = input().split()
        for i in num:
            l[j]+=int(i)
            j+=1
    print(max(l))
main()
