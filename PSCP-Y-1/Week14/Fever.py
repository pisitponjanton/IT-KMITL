"""Fever"""
def main(f):
    """Fever"""
    if 36<=f<38:
        print("No Fever")
    elif 38<=f<39:
        print("Mild Fever")
    elif 39<=f<40:
        print("High Fever")
    elif f>=40:
        print("Very High Fever")
main(float(input()))
