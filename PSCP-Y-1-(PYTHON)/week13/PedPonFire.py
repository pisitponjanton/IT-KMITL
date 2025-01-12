"""PedPonFire"""
def main(n):
    """PedPonFire"""
    d,l,s={},[],0
    for _ in range(n):
        num = int(input())
        if num not in d:
            d[num]=1
            l.append(num)
        else:
            d[num]+=1
    k=int(input())
    for i in l[:]:
        if k-i in l[:]:
            s += d[i]*d[k-i] if i != k-i else sum(range(1,d[i]))
            l.remove(i)
    print(s)
main(int(input()))
