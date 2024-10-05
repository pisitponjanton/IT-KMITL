"""RemoveTag"""
def main():
    """RemoveTag"""
    n = input()
    k=""
    k1=0
    if "<" in n:
        for i in n:
            if i==">":
                k1=1
            if k1 and not i in ("<",">"):
                k+=i
            if i=="<":
                k+=" "
                k1=0
        k=k.split()
    else:
        k=n.split()
    print(k)
    # print(n)
main()
