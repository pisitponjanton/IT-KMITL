"""isPrime_large"""
def main():
    """isPrime_large"""
    n = int(input())
    if n%2:
        t="YES" if n>1 else "NO"
        for i in range(3,int(n**0.5),2):
            if not n%i:
                t="NO"
    else:
        t="NO" if n>2 else "YES"
    print(t)
main()
