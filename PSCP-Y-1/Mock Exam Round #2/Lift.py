"""Lift"""
def main():
    """Lift"""
    n = int(input())
    wl = float(input())
    wa=0
    an=0
    for _ in range(n):
        age = int(input())
        wn = float(input())
        wa+=wn
        if age < 12:
            an+=0
        else:
            an+=1
    print("Safe" if (an>=1 and wa<=wl) or not n
    else "Not Safe")
main()
