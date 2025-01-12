"""Bonus"""
def main():
    """Bonus"""
    num = int(input())
    y = int(input())
    m = int(input())
    if m>=10:
        y+=1
    if y>20:
        y=20
    bonus = num*y
    print(5000 if bonus<5000 else 1000000
    if bonus>1000000 else bonus)
main()
