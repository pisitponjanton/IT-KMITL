"""[Final 2019] Tax"""
def main(y,cc,s):
    """[Final 2019] Tax"""
    if 1<=cc<=600:
        s = cc*0.5
    elif 601<=cc<=1800:
        s = (cc-600)*1.5+300
    elif cc>=1801:
        s = (cc-1800)*4+1800+300
    s-= (10/100)*s if y == 6 else (20/100)*s if y == 7 else (30/100)*s\
    if y == 8 else (40/100)*s if y == 9 else (50/100)*s if y>=10 else 0
    print(f"{s:.2f}")
main(int(input()),int(input()),0)
