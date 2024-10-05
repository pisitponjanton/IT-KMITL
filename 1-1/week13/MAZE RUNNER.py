"""MAZE RUNNER"""
def main():
    """MAZE RUNNER"""
    l1=[]
    for i in range(10):
        n = input()
        for z,j in zip(n,range(20)):
            if z.isspace():
                l1.append((i,j))
            elif z == 'X':
                l1.append(("x",i,j))
            elif z == 'Y':
                l1.append(("Y",i,j))
    print(l1)
main()
