"""Duplicate I"""
def main():
    """Duplicate I"""
    n = int(input())
    m = int(input())
    a = set()
    b = set()
    for _ in range(n):
        a.add(int(input()))
    for _ in range(m):
        b.add(int(input()))
    a = sorted(a.intersection(b))
    a.sort(reverse=True)
    if a:
        for i in a:
            print(i)
    else:
        print("Nope")
main()
