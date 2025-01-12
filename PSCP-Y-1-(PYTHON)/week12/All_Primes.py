"""All_Primes"""
def main():
    """All_Primes"""
    n = int(input())
    s=0
    for i in range(2,n+1):
        s+=1
        for j in range(i-1,1,-1):
            if not i%j:
                s-=1
                break
    print(s)
main()
