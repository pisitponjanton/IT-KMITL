"""PrasomSib"""
def main(n,ss=0):
    """PrasomSib"""
    for j,_ in enumerate(n):
        s=0
        for z in n[j:]:
            s+=int(z)
            if s>10:
                break
            if s==10:
                ss+=1
                break
    print(ss)
main(input())
