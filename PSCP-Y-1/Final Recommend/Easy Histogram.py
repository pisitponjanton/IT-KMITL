"""Easy Histogram"""
def main(n):
    """Easy Histogram"""
    l=[]
    for i in n:
        if i.isalpha():
            if all(j[0]!=i for j in l):
                l.append([i,1])
            else:
                for jj,j in enumerate(l):
                    if j[0]==i:
                        l[jj][1]+=1
                        break
    l.sort(key=lambda x: (x[0].lower(),x[0].isupper()))
    for i in l:
        print(f"{i[0]} = {i[1]}")
main(input())
