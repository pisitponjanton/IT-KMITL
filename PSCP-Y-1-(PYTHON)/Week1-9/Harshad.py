"""Harshad"""
def main():
    """Harshad"""
    a = []
    for _ in range(10):
        n = abs(int(input()))
        n1 = 0
        for i in str(n):
            n1+=int(i)
        if not n:
            a.append("No")
        else:
            if not n%n1:
                a.append("Yes")
            else:
                a.append("No")
    for i in a:
        print(i)
main()
