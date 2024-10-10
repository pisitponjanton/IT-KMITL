"""Century"""
def main():
    """Century"""
    n = int(input())
    l = []
    for _ in range(n):
        pk = input()
        pk1=""
        pk2=""
        n1=0
        pk3=0
        for i in pk:
            if i.isnumeric():
                pk1+=i
            else:
                pk2+=i
        if pk2.strip() == "B.E.":
            pk1 = int(pk1)-543
        pk1 = int(pk1)/100
        for i in str(pk1):
            if i == ".":
                pk3=int(str(pk1)[n1+1:])
            n1+=1
        if 0<pk1*100<=100:
            pk1 = 1
        elif pk1*100 > 100:
            pk1 = int(pk1) if not pk3 else int(pk1)+1
        else:
            pk1 = "ERROR"
        l.append(pk1)
    for i in l:
        print(i)
main()
