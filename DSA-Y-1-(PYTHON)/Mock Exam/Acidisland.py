"""Acidisland"""
def m_t(grid,c,r,x):
    """mm"""
    l = []
    for z in range(0,x):
        l_l = []
        for i in grid[c:c+z+1]:
            for j in i[r:r+z+1]:
                l_l.append(j)
        if all(l_l):
            l.append(l_l)
    return l
def main(l):
    """Acidisland"""
    l = [int(i) for i in l]
    x,y = l[0],l[1]
    grid = []
    for i in range(x):
        grid.append([int(j) for j in input().split()])
    num_list = []
    for i in range(y):
        for j in range(x):
            num_list.append(m_t(grid,i,j,max(x,y)))
    sum_n = []
    for i in num_list:
        for j in i:
            sum_n.append(sum(j))
    for i in range(min(x,y),-1,-1):
        if i*i in sum_n:
            print(i*i)
            return
    print(0)
main(input().split())
