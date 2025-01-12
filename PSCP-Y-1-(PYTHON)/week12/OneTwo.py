"""OneTwo"""
def onetwo(n):
    """OneTwo"""
    if n<3:
        return str(n)
    return str(onetwo(n-1))+str(onetwo(n-2))
def main():
    """OneTwo"""
    n = onetwo(int(input()))
    print(n)
main()
