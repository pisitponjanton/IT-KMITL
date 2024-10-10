"""HorizontalHistogram"""
def mm(x):
    """mmfe"""
    n=""
    for i in range(x):
        if not i%5 and i:
            n+="|"
        n+="-"
    return n
def main():
    """HorizontalHistogram"""
    n = input()
    num=""
    l = []
    l2 = []
    for i in n:
        l.append([i,n.count(i)])
    for i in l:
        if not i in l2:
            l2.append(i)
    l2.sort(key=lambda x: (x[0].isupper(),x[0]))
    for i in l2:
        num = mm(i[1])
        print(f"{i[0]} : {num}")
main()
