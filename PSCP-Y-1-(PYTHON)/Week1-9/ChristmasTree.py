"""ChristmasTree"""
def main():
    """ChristmasTree"""
    num1 = int(input())
    num2 = int(input())
    n = num1-1
    i=1
    for _ in range(1,num1+1):
        print(f"{' '*n}{'*'*i}")
        i+=2
        n-=1
    for _ in range(1,num2+1):
        print(f"{' '*(num1-2)}{'---'}")
main()
