"""BloodDonation"""
def main():
    """BloodDonation"""
    age = int(input())
    w = int(input())
    n = int(input())
    a = 17<=age<=70
    b = w>=45
    p=1
    if not n:
        a = 17<=age<=55
    if age==17 or 60<=age<=70:
        p = 1 if input()=="True" else 0
    print("Yes" if a and p and b else "No")
main()
