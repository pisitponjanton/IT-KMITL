"""[Final 2020] Lucky Number"""
def main(n):
    """[Final 2020] Lucky Number"""
    r=1
    n = [i for i in n if i%2 ]
    if len(n)>=2:
        while len(n)>=n[r]:
            n = [i for j,i in enumerate(n) if (j+1)%n[r]]
            r+=1
            if r>=len(n):
                break
    print(*n)
main(list(range(1,int(input())+1)))
