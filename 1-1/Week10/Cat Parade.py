"""Cat Parade"""
def main():
    """Cat Parade"""
    l=[]
    l1=[]
    l2=[]
    while True:
        num = input().split(",")
        if num == ['END']:
            break
        if num!=['IT\'S A DOG']:
            for i in num:
                l.append(i.strip())
        else:
            l.pop()
    j=0
    for i in l:
        if not i in l2:
            l1.append(l[j]+" "+str(j+1)+" "+str(l.count(i)))
            l2.append(i)
        j+=1
    l1.sort()
    for i in l1:
        print(i)
main()
