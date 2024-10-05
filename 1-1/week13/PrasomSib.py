"""PrasomSib"""
def main():
    """PrasomSib"""
    n = input()
    z=1
    r=0
    for i in n:
        s=int(i)
        for j in n[z:]:
            s+=int(j)
            if s==10:
                r+=1
                break
            if s>10:
                break
        z+=1
    print(r)
main()
