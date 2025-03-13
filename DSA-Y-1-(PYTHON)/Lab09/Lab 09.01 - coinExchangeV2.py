"""Lab 09.01 - coinExchangeV2"""
import json

def num_grid(d,g):
    """num to num"""
    d3 = []
    for indexij,i in enumerate(d):
        de = sum(i1*i2 for i1,i2 in i.items())
        if de < indexij+1:
            if g[indexij-de]:
                i.update(g[indexij-de])
        d3.append(i)
    return d3
def num_num(d1,d2):
    d3 = []
    for i,j in zip(d1,d2):
        numsumD1 = sum(i1*i2 for i1,i2 in i.items())
        numsumD2 = sum(j1*j2 for j1,j2 in j.items())
        sumcoinD1 = sum(i1 for i1 in i.values())
        sumcoinD2 = sum(j1 for j1 in j.values())
        if numsumD1 == numsumD2:
            if sumcoinD1 < sumcoinD2:
                d3.append(i)
            elif sumcoinD1 > sumcoinD2:
                d3.append(j)
            else:
                if i and j:
                    if list(j.items())[-1][-1] > list(i.items())[-1][-1]:
                        d3.append(i)
                    else:
                        d3.append(j)
                else:
                    if len(j) > len(i):
                        d3.append(i)
                    else:
                        d3.append(j)
        elif numsumD1 > numsumD2:
            d3.append(i)
        else:
            d3.append(j)
    return d3
def coin(x, l):
    """Lab 09.01 - coinExchangeV2"""
    grid,gridlast = [],[]
    grid.append([{}]*x)
    gridlast.append([{}]*x)
    l = {i:j for i,j in sorted(l.items(),key=lambda x: int(x[0]))}
    for i in l:
        coin = int(i)
        dictnum = []
        dictnum.append([{}]*x)
        for coins in range(1,l[i]+1):
            dictC = []
            for indexJ in range(1,x+1):
                if coins*coin <= indexJ:
                    dictC.append({coin:coins})
                else:
                    dictC.append({})
            dictC = num_grid(dictC,grid[-1])
            dictC = num_num(dictnum[-1],dictC)
            dictnum.append(dictC)
        grid.append(num_num(grid[-1],dictnum[-1]))
    r = grid[-1][x-1]
    for i in l:
        r.setdefault(int(i),0)
    r = {i:j for i,j in sorted(r.items(),key=lambda x: -int(x[0]))}
    sumnum = sum(i*j for i,j in r.items())
    print(f"Amount: {x}")
    if sumnum >= x:
        print("Coin exchange result:")
        for i,j in r.items():
            print(f"  {i} baht = {j} coins")
        print(f"Number of coins: {sum(i for i in r.values())}")
        return
    print("Can not exchange.")
coin(int(input()), json.loads(input()))
