"""CoPrimeV1"""
def main():
    """CoPrimeV1"""
    n1 = int(input())
    n2 = int(input())
    for i in range(min(n1,n2),-1,-1):
        if 0 in (n1,n2):
            print("YES" if max(n1,n2)==1 else "NO")
            print(max(n1,n2))
            break
        if not n1%i and not n2%i:
            print("YES" if i==1 else "NO")
            print(i)
            break
main()
