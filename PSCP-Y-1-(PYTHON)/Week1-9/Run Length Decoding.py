"""Run Length Decoding"""
def main():
    """Run Length Decoding"""
    n = input()
    t = ''
    for i in n:
        if i.isnumeric():
            t = str(t)+str(i)
        else:
            print(f"{int(t)*i}",end='')
            t=0
    print()
main()
