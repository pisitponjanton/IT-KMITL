"""BTSMRT"""
def main():
    """BTSMRT"""
    t = input()
    age = float(input())
    h = float(input())
    if age <14 and h < 90:
        print("FREE")
    elif t == "Children Day":
        if age < 14 and h <= 140:
            print("FREE")
        else:
            print("PAY")
    elif t == "Senior Day":
        if age >= 60:
            print("FREE")
        else:
            print("PAY")
    else:
        print("PAY")
main()
