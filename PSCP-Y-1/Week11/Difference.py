"""Difference"""
def main():
    """Difference"""
    n = int(input())
    m = int(input())
    a = set()
    b = set()
    for _ in range(n):
        a.add(int(input()))
    for _ in range(m):
        b.add(int(input()))
    a = sorted(a.difference(b))
    for i in a:
        print(i,end=" ")
main()