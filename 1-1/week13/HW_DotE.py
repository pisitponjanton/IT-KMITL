"""HW_DotE"""
import math
def main(n):
    """HW_DotE"""
    c = 0
    for k in range(max(0,n-5), min(5,n)+1):
        if abs(2 * k - n) <= 1:
            r = math.comb(n, k)
            c += r
    print(c)
main(int(input()))
