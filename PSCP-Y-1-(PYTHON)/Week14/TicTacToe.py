"""TicTacToe"""
def main(s="",n=0):
    """TicTacToe"""
    x,o = [],[]
    for _ in range(3):
        s+=input()
    for i in s:
        if i == "X":
            x.append(n)
        elif i == "O":
            o.append(n)
        n+=1
    x1,x2=all(i in x for i in (0,1,2)) or all(i in x for i in (3,4,5))\
    or all(i in x for i in (6,7,8)) or all(i in x for i in (0,3,6))\
    ,all(i in x for i in (1,4,7)) or all(i in x for i in (2,5,8))\
    or all(i in x for i in (0,4,8)) or all(i in x for i in (2,4,6))
    o1,o2=all(i in o for i in (0,1,2)) or all(i in o for i in (3,4,5))\
    or all(i in o for i in (6,7,8)) or all(i in o for i in (0,3,6))\
    ,all(i in o for i in (1,4,7)) or all(i in o for i in (2,5,8))\
    or all(i in o for i in (0,4,8)) or all(i in o for i in (2,4,6))
    if x1 or x2:
        print("X WIN")
    elif o1 or o2:
        print("O WIN")
    else:
        print("DRAW")
main()
