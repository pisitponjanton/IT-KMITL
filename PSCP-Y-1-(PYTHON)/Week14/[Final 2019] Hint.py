"""[Final 2019] Hint"""
def mn(n):
    """input().split()"""
    a=[]
    if n[0] == ">=":
        for i in range(int(n[1]),10):
            a.append(str(i))
    elif n[0] == "<=":
        for i in range(int(n[1]),-1,-1):
            a.append(str(i))
    elif n[0] == ">":
        for i in range(int(n[1])+1,10):
            a.append(str(i))
    elif n[0] == "<":
        for i in range(int(n[1])-1,-1,-1):
            a.append(str(i))
    elif n[0] == "!=":
        for i in range(10):
            if i==int(n[1]):
                continue
            a.append(str(i))
    else:
        a.append(n[1])
    a.sort()
    return a
def main(n1,n2,n3):
    """[Final 2019] Hint"""
    for i in mn(n3):
        for j in mn(n2):
            for z in mn(n1):
                print(i+j+z)
main(input().split(),input().split(),input().split())
