"""Saint Seiya"""
def main():
    """Saint Seiya"""
    num = int(input())
    numf = int(input())
    n = numf//331
    tt = num//6
    t = num - 6*n if n<=tt else num - 6*tt
    u = 165 if 2<=t<4 else 330 if 4<=t<6 else 331 if t==6 else 0
    saint = 331*n if n<=tt else 331*tt
    tf = numf - saint if n<=tt else u+(331*tt) - saint
    if 0<tf<=165:
        t-=2
        saint+=165
    elif 165<tf<=330:
        t-=4
        saint+=330
    elif tf == 331:
        t-=6
        saint+=331
    saint+=(t-1)*12 if t>0 else 0
    print(saint if num > 1 else 0)
main()
