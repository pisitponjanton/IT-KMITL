"""Lab 09.03 - Longest Common Substring"""
def main(x,y):
    """Lab 09.03 - Longest Common Substring"""
    grid = []
    for i,_ in enumerate(x):
        sublist = []
        for indexj,j in enumerate(y):
            if j == x[i] and grid and j:
                sublist.append(grid[i-1][indexj-1]+1)
            elif j == x[i]:
                sublist.append(1)
            else:
                sublist.append(0)
        grid.append(sublist)
    max_num ,lastindex= 0,0
    for i in grid:
        for indexJ,j in enumerate(i):
            if j > max_num:
                max_num = j
                lastindex = indexJ
    text = y[lastindex-max_num+1:lastindex+1]
    print(text+"\n"+str(max_num) if max_num else "No common substring.")
main(input(),input())
