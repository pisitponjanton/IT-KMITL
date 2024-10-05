"""Heron of Alexandria"""
def main():
    """Heron of Alexandria"""
    a = float(input())
    b = float(input())
    c = float(input())
    s = (a+b+c)/2
    area = (s*(s-a)*(s-b)*(s-c))**0.5
    print(f"{area:.3f}")
main()
