"""Right Arrow"""
def main():
    """Right Arrow"""
    num1 = int(input())
    num2 = int(input())
    n = num2//2
    n1 = 0
    for z in range(1,num2+1):
        if z <= n+1:
            n1+=1
        if z > n+1:
            n1-=1
        print(f"{' '*(n1-1)}{'*'*num1}",end='')
        print()
main()
