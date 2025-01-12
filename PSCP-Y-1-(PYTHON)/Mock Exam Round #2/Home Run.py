"""Home Run"""
def main():
    """Home Run"""
    n = int(input())
    spy = float(input())
    num = 0
    for _ in range(n):
        sa = float(input())
        if sa < spy:
            num+=1
    print(num)
main()
