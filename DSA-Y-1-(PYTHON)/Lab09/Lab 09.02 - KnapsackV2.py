"""Lab 09.02 - KnapsackV2"""
import json
def main(l,x):
    """Lab 09.02 - KnapsackV2"""
    grid = []
    for index,i in enumerate(l):
        c = []
        coc = []
        if grid:
            cc = grid[-1].copy()
        for j in range(x):
            if i[2] <= j+1:
                c.append([i])
            else:
                c.append([])
        if index:
            for indexR,r in enumerate(c):
                if r:
                    xx = sum(i1[2] for i1 in r)
                    if xx < indexR+1:
                        if cc[indexR-xx]:
                            c[indexR]+=(cc[indexR-xx])
            for z,z1 in zip(cc,c):
                if z and z1:
                    x1 = sum(i1[1] for i1 in z)
                    x2 = sum(i1[1] for i1 in z1)
                    if x1 > x2:
                        coc.append(z)
                    else:
                        coc.append(z1)
                elif z:
                    coc.append(z)
                elif z1:
                    coc.append(z1)
                else:
                    coc.append(z)
            grid.append(coc)
        else:
            grid.append(c)
        
    finallist = grid[-1][-1]
    finallist.sort(key = lambda x: x[0] )
    print(f"Total: {sum(i1[1] for i1 in finallist)}")
    for i in finallist:
        print(f"{i[0]} -> {i[2]} kg -> {i[1]} THB")
main(json.loads(input()),int(input()))
