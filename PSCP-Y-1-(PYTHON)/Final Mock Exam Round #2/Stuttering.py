"""Stuttering"""
def main(x):
    """Stuttering"""
    l=[]
    for j,i in enumerate(x):
        if j>0:
            if i!=x[j-1]:
                l.append(i)
        else:
            l.append(i)
    print(*l)
main(input().split())
