"""Easy Histogram No Dict"""
def main():
    """Easy Histogram No Dict"""
    num = input()
    n = []
    n1 = []
    for i in num:
        if not i.isspace() :
            n.append([i,num.count(i)])
    for i in n:
        if not i in n1:
            n1.append(i)
    n1.sort(key=lambda x: (x[0].lower(),x[0].isupper()))
    for i in n1:
        print(f"{i[0]} = {i[1]}")
main()
