"""[Final 2020] RunGame"""
def main(n):
    """[Final 2020] RunGame"""
    l=[]
    for i,j in enumerate(n):
        if i<len(n)-1:
            l.append(abs(int(n[i+1])-int(j)))
    print(sum(l))
main([0]+input().split())
