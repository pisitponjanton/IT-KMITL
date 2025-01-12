"""ValidVar"""
def main():
    """ValidVar"""
    n = int(input())
    s = 0
    l = []
    for _ in range(0,n):
        t = input().strip()
        for i in t:
            if not i.isalnum() and not i =="_":
                s=1
        for i in t[1:-1]:
            if i.isspace():
                s=1
        if t[0].isnumeric() or s:
            l.append("Invalid")
        elif t in ("if","else","elif","while","for","True","False","continue","break"):
            l.append("Invalid")
        elif t in ("return","is","in","and","or","from","as","pass","not","def","None","import"):
            l.append("Invalid")
        else:
            l.append("Valid")
        s=0
    for i in l:
        print(i)
main()
