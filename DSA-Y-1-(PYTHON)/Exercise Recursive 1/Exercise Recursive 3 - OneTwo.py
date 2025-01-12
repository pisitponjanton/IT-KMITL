"""Exercise Recursive 3 - OneTwo"""
def onetwo(n):
    """OneTwo"""
    if n>2:
        return onetwo(n-1) + onetwo(n-2)
    else:
        return str(n)
def main(x):
    """main"""
    print(onetwo(x))
main(int(input()))