"""GCD_v1"""
def main():
    """GCD_v1"""
    n1 = int(input())
    n2 = int(input())
    for i in range(min(n1,n2),-1,-1):
        if 0 in (n1,n2):
            print(max(n1,n2))
            break
        if not n1%i and not n2%i:
            print(i)
            break
main()
