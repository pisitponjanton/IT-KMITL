"""[Final 2020] Pad Thai"""
def main():
    """[Final 2020] Pad Thai"""
    f,r,r1=[],[],0
    l= ["Pad Thai Sauce","Tofu","Pickle Turnip","Shrimp","Bean Sprouts",
    "Noodle","Chives","Lime","Egg","Oil","Peanuts"]
    lr=["Sweet","Sour","Salty"]
    while True:
        n = input()
        if n=="End":
            break
        if n == "Cook":
            r1=1
            continue
        if not r1:
            f.append(n)
        else:
            r.append(n)
    nf = [i for i in f if not i in l]
    if nf:
        print("This is not Pad Thai!!!")
    elif all(i in l for i in f) and all(i in lr for i in r) \
    and len(set(f)) == 11 and len(set(r)) == 3:
        print("Delicious!")
    elif all(i in l for i in f) and len(set(f)) == 11:
        print("Not Bad...")
    else:
        print("This is bad!")
main()
