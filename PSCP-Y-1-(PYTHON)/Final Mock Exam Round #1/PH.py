"""PH"""
def main(x):
    """PH"""
    if 0<=x<7:
        print("acidic")
    elif x==7:
        print("neutral")
    elif 7<x<=14:
        print("akaline")
    else:
        print("error")
main(float(input()))
