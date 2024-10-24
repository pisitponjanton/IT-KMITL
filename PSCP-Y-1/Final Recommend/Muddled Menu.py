"""Muddled Menu"""
def main():
    """"Muddled Menu"""
    l=[]
    while True:
        n = input()
        if "DONE" == n:
            break
        if "CLOSED" == n:
            l.clear()
            break
        if "SOMETHING'S WRONG" == n:
            l.clear()
            continue
        if "Can't do: " in n:
            n=n.split(": ")
            l.remove(n[1])
            continue
        n=n.split(" #")
        if n[1]=="N":
            l.append(n[0])
        else:
            l.insert(int(n[1])-1,n[0])
    lr=l.copy()
    lr.reverse()
    print(f"Full Course: {l} Reversed: {lr}")
main()
