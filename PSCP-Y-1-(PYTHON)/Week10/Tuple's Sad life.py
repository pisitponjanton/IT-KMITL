"""Tuple's Sad life"""
def main():
    """Tuple's Sad life"""
    t = input().split()
    n = input()
    num = t.index(n)
    for _ in range(t.count(n)):
        for _ in range(t.count(n)):
            print(num,end=" ")
        print()
main()
