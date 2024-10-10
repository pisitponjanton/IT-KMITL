"""Ink"""
import math
def main(n):
    """Ink"""
    for _ in range(int(n[1])):
        d = input().split()
        print(math.ceil((3.1416*(((int(d[0])**2+int(d[1])**2)**0.5))**2)/int(n[0])))
main(input().split())
