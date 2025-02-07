""""Labs 05.04 - Calculator"""
def main(x):
    """main"""
    s = 0
    for i in range(1,x+1):
        s += len(str(i))+1
    print(s)
main(int(int(input())))
