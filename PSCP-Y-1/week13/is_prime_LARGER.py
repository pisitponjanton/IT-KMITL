"""is_prime_LARGER"""
def main(n):
    """is_prime_LARGER"""
    t=1
    for i in range(2,int(n**0.5)+1,3):
        if not n%i:
            t=0
            break
    print("True" if t and n>1 else "False")
main(int(input()))
