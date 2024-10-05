"""Calculator"""
def main():
    """Calculator"""
    n = int(input())
    num=0
    if n>1:
        for i in range(1,n+1):
            num+=len(str(i))+1
    else:
        num=1
    print(num)
main()
