"""BigFrame"""
def check(x):
    """BigFrame"""
    xt = ''
    for i in x[::-1]:
        if i.isspace() and not xt:
            pass
        else:
            xt += i
    return xt[::-1]
def main():
    """BigFrame"""
    n1 = input()
    n2 = input()
    n3 = input()
    n4 = input()
    n5 = input()
    n1 = check(n1)
    n2 = check(n2)
    n3 = check(n3)
    n4 = check(n4)
    n5 = check(n5)
    s = max(len(n1),len(n2),len(n3),len(n4),len(n5))
    print("*"*(s+4))
    print(f"* {n1:<{s}} *")
    print(f"* {n2:<{s}} *")
    print(f"* {n3:<{s}} *")
    print(f"* {n4:<{s}} *")
    print(f"* {n5:<{s}} *")
    print("*"*(s+4))
main()
