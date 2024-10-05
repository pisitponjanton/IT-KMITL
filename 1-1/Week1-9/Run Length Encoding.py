"""Run Length Encoding"""
def main():
    """Run Length Encoding"""
    n = input()
    s = 0
    t=0
    n1 = ''
    for i in n:
        if i == n[s]:
            t+=1
            n1 = i
        else:
            print(f"{t}{n1}",end='')
            n1 = i
            s+=t
            t=1
    print(f"{t}{n1}",end='')
    print()
main()
