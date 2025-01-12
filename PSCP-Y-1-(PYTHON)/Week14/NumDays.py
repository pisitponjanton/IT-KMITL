"""NumDays"""
def main(d1,m1,d2,m2):
    """NumDays"""
    d={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    print(abs((sum(d[i] for i in range(1,m1+1))-(d[m1]-d1))-\
    (sum(d[i] for i in range(1,m2+1))-(d[m2]-d2)))\
    if d1<=d[m1] and d2<=d[m2] else "Impossible")
main(int(input()),int(input()),int(input()),int(input()))
