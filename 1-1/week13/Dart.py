"""Dart"""
def main():
    """Dart"""
    s=0
    for _ in range(int(input())):
        n = input().split()
        r = (int(n[0])**2 + int(n[1])**2)**0.5
        s+= 5 if r<=2 else 4 if 2<r<=4 else 3 if 4<r<=6 else 2 if 6<r<=8 else 1 if 8<r<=10 else 0
    print(s)
main()
