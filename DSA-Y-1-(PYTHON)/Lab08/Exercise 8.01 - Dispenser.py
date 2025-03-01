"""Exercise 8.01 - Dispenser"""
def new_sort(x):
    """new sort"""
    if len(x[-1]) >= 2:
        return -int(x[-1][0]) , -int(x[-1][1]) ,0 , 0 , 0, -len(x)
    if len(x) == 2 :
        return -int(x[-1]) , -int(x[-2]),0 , 0 , 0,  -len(x)
    if len(x) == 3 :
        return -int(x[-1]) , -int(x[-2]) , -int(x[-3]) , 0 , 0 ,-len(x)
    if len(x) == 4 :
        return -int(x[-1]) , -int(x[-2]) , -int(x[-3]) , -int(x[-4]) , 0 , -len(x)
    if len(x) >= 5 :
        return -int(x[-1]) , -int(x[-2]) , -int(x[-3]) , -int(x[-4]) , -int(x[-5]) , -len(x)
    return -int(x[-1][0]) , 0 , 0 , 0 , 0, -len(x)

def new_sort_1(x):
    """new sort"""
    if len(x[-1]) >= 2:
        return -int(x[-1][0]) , -int(x[-1][1]) ,0 , 0 , 0, len(x)
    if len(x) == 2 :
        return -int(x[-1]) , -int(x[-2]),0 , 0 , 0,  len(x)
    if len(x) == 3 :
        return -int(x[-1]) , -int(x[-2]) , -int(x[-3]) , 0 , 0 ,len(x)
    if len(x) == 4 :
        return -int(x[-1]) , -int(x[-2]) , -int(x[-3]) , -int(x[-4]) , 0 , len(x)
    if len(x) >= 5 :
        return -int(x[-1]) , -int(x[-2]) , -int(x[-3]) , -int(x[-4]) , -int(x[-5]) , len(x)
    return -int(x[-1][0]) , 0 , 0 , 0 , 0, len(x)

def num(l):
    s1,s2="",""
    l1, l2 = [i[:] for i in l],[i[:] for i in l]
    while l1:
        l1.sort(key = new_sort)
        s1 += l1[0].pop()
        l1 = [i for i in l1 if i]
    while l2:
        l2.sort(key = new_sort_1)
        s2 += l2[0].pop()
        l2 = [i for i in l2 if i]
    return max(int(s1),int(s2))

def main(m,n):
    """Exercise 8.01 - Dispenser"""
    l=[[] for _ in range(n)]
    for _ in range(m):
        inp = input().split()
        for i,j in zip(l,inp):
            i.append(j)
    print(num(l))
main(int(input()),int(input()))
