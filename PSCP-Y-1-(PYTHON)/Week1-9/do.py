"""f"""
def main():
    """f"""
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    p = a*b
    box = b+c
    s = d//box
    r = d%box
    rp = a*r
    snum = s*p
    if r >= b:
        s+=1
        box=box*s
        snum = s*p
    else:
        box=(box*s)+r
        snum = snum+rp
    print(f"{snum} {box}")
main()
