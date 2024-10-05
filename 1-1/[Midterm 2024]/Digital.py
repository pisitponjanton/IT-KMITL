"""Digital"""
def main():
    """Digital"""
    name = input()
    thai = input()
    home = input()
    age = float(input())
    money = float(input())
    bk = float(input())
    n1 =  thai in ("Yes","True") and home in ("Yes","True")
    n2 = age >= 16 and bk <= 500000 and money <= 840000
    if n1 and n2:
        print(f"Congratulations! {name} is qualified to receive a digital",end=" ")
        print("wallet amount of 10,000 baht, sponsored by all taxpayers in Thailand.")
    else:
        print(f"Unfortunately, {name} is not qualified.")
main()
