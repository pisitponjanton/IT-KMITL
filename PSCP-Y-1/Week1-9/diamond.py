"""diamond"""
def diamond():
    """diamond"""
    num = int(input())
    n=1
    n1 = num//2 - 1
    print(f"{'*':^{num}}")
    for _ in range(1,n1+1):
        print(f"{' '*n1}*{' '*n}*")
        n+=2
        n1-=1
    print("*"*num)
    n1 = num//2 - 1
    n2 = 1
    for _ in range(1,n1+1):
        print(f"{' '*n2}*{' '*(n-2)}*")
        n-=2
        n2+=1
    print(f"{'*':^{num}}")
diamond()
