"""Amefuri Plus"""
def main():
    """Amefuri Plus"""
    h = int(input())
    t = input()
    wet = 8
    for i in t:
        if not wet:
            break
        if wet > 16 :
            wet = 16
        if i in ("R","r"):
            wet+=2
        elif i in ("H","h"):
            wet = "LOL"
            break
        elif i in ("S","s"):
            wet+=3
        elif 0 <= h < 6 or 18 <= h <= 24:
            wet -= 0.25 if i in ("C","c") else 0.5 if i in ("N","n") else 0.75
        elif 6 <= h < 18:
            wet -= 0.5 if i in ("C","c") else 1 if i in ("N","n") else 1.5
        h+=1
        if h>24:
            h=1
    print("Dry" if not wet else "Lost" if wet == "LOL" else f"Still Wet (Wet Level: {wet:.2f})")
main()
