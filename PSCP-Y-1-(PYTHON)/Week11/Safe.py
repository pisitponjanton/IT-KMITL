"""Safe"""
def main():
    """Safe"""
    n1 = input()
    n2 = input()
    n1 = [ord(i)-ord("A")+1 for i in n1]
    n2 = [ord(i)-ord("A")+1 for i in n2]
    k=0
    for i,j in zip(n1,n2):
        num=abs(i-j)
        if num>13:
            n=min(i,j)+26
            num=abs(n-max(i,j))
        k+=num
    print(k)
main()
