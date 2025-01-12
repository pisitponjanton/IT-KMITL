"""Meteorite"""
def main():
    """Meteorite"""
    a = float(input())
    b = int(input())
    c = float(input())
    n=0
    num=0
    while a >= c:
        a/=b
        n+=1
    for i in range(n):
        num+=b**i
    print(num)
main()
