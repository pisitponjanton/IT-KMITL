"""WordSequence II"""
def main():
    """WordSequence II"""
    n1 = input()
    n2 = input()
    l=0
    m,n = len(n1),len(n2)
    for _ in range(max(m,n)):
        print(n2[:l]+n1[l:])
        l+=1
    print(n2)
main()
