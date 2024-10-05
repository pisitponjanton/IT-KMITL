"""Align"""
def main():
    """Align"""
    num = int(input())
    a = input()
    n = input()
    print(f"{n:>{num}}" if a == "right" else f"{n:<{num}}" if a=="left"
    else f"{n:^{num+1}}" if a == "center" else "")
main()
