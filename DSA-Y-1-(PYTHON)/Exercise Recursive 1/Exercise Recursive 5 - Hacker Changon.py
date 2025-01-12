"""Exercise Recursive 5 - Hacker Changon"""
def hackerChangon(n,m):
    """Hacker Changon"""
    print(n)
    if n!=m and n<=m:
        hackerChangon(n+1,m)
    elif n!=m and n>m:
        hackerChangon(n-1,m)
def main(n,m):
    """main"""
    hackerChangon(n,m)
main(int(input()),int(input()))