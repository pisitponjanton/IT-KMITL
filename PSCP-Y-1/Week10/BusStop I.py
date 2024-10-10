"""BusStop I"""
def main():
    """BusStop I"""
    p = int(input())
    n = int(input())
    l=[]
    busstop = []
    bus=[]
    for _ in range(n):
        num = input().split()
        l.append(num)
    l.sort(key=lambda x: int(x[0]))
    for i in l:
        busstop.append(i[0])
    k=0
    s=0
    for i in l:
        for j in i[1:]:
            if j in busstop[k:] and len(bus)<p:
                bus.append(j)
        k+=1
        for z in bus[:]:
            if z == busstop[k]:
                bus.remove(z)
                s+=1
    print(s)
main()
