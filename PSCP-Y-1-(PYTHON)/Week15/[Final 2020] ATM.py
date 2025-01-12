"""[Final 2020] ATM"""
def main(n):
    """[Final 2020] ATM"""
    while True:
        t = input().split()
        if "END" in t:
            break
        if t[0]=="D":
            n+=int(t[1])
        else:
            n-=int(t[1]) if int(t[1])<n else n
    print(n)
main(int(input()))
