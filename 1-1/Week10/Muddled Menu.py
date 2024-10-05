"""Muddled Menu"""
def menu():
    """Muddled Menu"""
    l1=[]
    while True:
        n = input()
        if n == "DONE":
            break
        if n == "CLOSED":
            l1.clear()
            break
        if n == "SOMETHING'S WRONG":
            l1.clear()
        elif " #N" in n:
            l1.append(n.replace(" #N",""))
        elif not "Can't do: " in n:
            n=n.split(" #")
            l1.insert(int(n[1])-1,n[0])
        else:
            l1.remove(n.replace("Can't do: ",""))
    l2=l1.copy()
    l2.reverse()
    print("Full Course:",l1,"Reversed:",l2)
menu()
