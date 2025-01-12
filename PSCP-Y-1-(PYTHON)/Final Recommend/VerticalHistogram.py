"""VerticalHistogram"""
def main(n):
    """VerticalHistogram"""
    d={i:n.count(i) for i in n if i.isalpha()}
    m=max(d.values())
    d=sorted(d.items())
    for _ in range(m):
        print(f" {m}" if m<10 else m,end="  ")
        for _,j in d:
            if j>=m:
                print("*",end=' ')
            else:
                print(" ",end=' ')
        print()
        m-=1
    print('    ',end='')
    for i,_ in d:
        print(i,end=" ")
main(input())
