"""Heads and Legs"""
def main(a,b):
    """Heads and Legs"""
    print(f"{b//2-a} {2*a-b//2}" if b//2-a>=0 and 2*a-b//2>=0 and \
    (b//2-a)*4+(2*a-b//2)*2==b else "Impossible")
main(int(input()),int(input()))
