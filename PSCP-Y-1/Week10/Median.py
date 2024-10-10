"""Median"""
def main():
    """Median"""
    n = int(input())
    o = []
    for _ in range(n):
        num = float(input())
        o.append(num)
    o.sort()
    y = o[((n+1)//2)-1]
    if n%2:
        print(f"{float(y):.3f}")
    else:
        y1 = o[((n+1)//2)]
        print(f"{(float(y)+float(y1))/2:.3f}")
main()
