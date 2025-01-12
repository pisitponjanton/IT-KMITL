"""Easy Histogram"""
def numm(n,f):
    """Amazon"""
    s=0
    for i in n:
        if i == f:
            s+=1
    return s
def main():
    """Easy Histogram"""
    num = input()
    n = []
    n1 = []
    for i in num:
        if not i.isspace() :
            n.append([i,numm(num,i)])
    for i in n:
        if not i in n1:
            n1.append(i)
    n1.sort(key=lambda x: (x[0].lower(),x[0].isupper()))
    for i in n1:
        print(f"{i[0]} = {i[1]}")
main()
