"""[Final 2020] Area"""
def main(s=0):
    """[Final 2020] Area"""
    for _ in range(int(input())):
        s+=sum((1 for i in input() if not i.isspace()))
    print(s)
main()
