"""Cat Parade"""
def main():
    """Cat Parade"""
    l,s=[],0
    while True:
        n = input().split(", ")
        if 'END' in n:
            break
        if "IT'S A DOG" in n:
            l.pop()
            s-=1
            continue
        for i in n:
            s+=1
            if all(i != j[0] for j in l):
                l.append([i,s,1])
            else:
                for t,j in enumerate(l):
                    if j[0] == i:
                        l[t][2]+=1
                        break
    l.sort()
    for i in l:
        print(*i)
main()
