"""Mastermind"""
def main(n1,n2,s=""):
    """Mastermind"""
    l,n11=[],[]
    for r,(i,j) in enumerate(zip(n1,n2)):
        if i==j:
            s+="B"
            l.append(r)
        else:
            n11.append(i)
    if len(s)<4:
        for j,i in enumerate(n2):
            if i in n11[:] and j not in l:
                s+="W"
                n11.remove(i)
    while len(s)<4:
        s+="O"
    print(s)
main(list(input()),list(input()))
