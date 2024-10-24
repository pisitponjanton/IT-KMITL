"""Diamond I"""
def main(n,m):
    """Diamond I"""
    l=[0]*m
    for _ in range(n):
        n=input().split()
        for i in range(m):
            l[i]+=int(n[i])
    print(max(l))
main(int(input()),int(input()))
