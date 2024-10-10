"""Majority"""
def main(k,n):
    """Majority"""
    d={}
    for i in range(1,k+1):
        d[i]=0
    for i in range(n):
        d[int(input())]+=1
    if max(d.values()) >= n//2:
        for i,j in d.items():
            if j == max(d.values()):
                print(i,j)
                break
    else:
        print(0,max(d.values()))
main(int(input()),int(input()))
