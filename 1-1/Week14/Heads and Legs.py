"""Heads and Legs"""
def main(a,b):
    """Heads and Legs"""
    lr = b//4
    b = a-lr
    r = a-b
    print(f"{b,r}"if b//2 > a else "Impossible")
main(int(input()),int(input()))
