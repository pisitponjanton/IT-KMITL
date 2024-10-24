"""Facebook"""
def main():
    """Facebook"""
    d,l={},[]
    while True:
        n=input()
        if "?" in n:
            n=n.split(" ? ")
            if n[0] in d and n[1] in d:
                l=list(set(d[n[0]]).intersection(set(d[n[1]])))
            if l:
                l.sort()
                for i in l:
                    print(i)
            else:
                print("No mutual friend")
            break
        n=n.split(" <-> ")
        if n[0] not in d:
            d[n[0]]=[n[1]]
        else:
            d[n[0]]+=[n[1]]
        if n[1] not in d:
            d[n[1]]=[n[0]]
        else:
            d[n[1]]+=[n[0]]
main()
