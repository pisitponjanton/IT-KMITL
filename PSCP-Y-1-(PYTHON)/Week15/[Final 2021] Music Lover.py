"""[Final 2021] Music Lover"""
def main():
    """[Final 2021] Music Lover"""
    d={}
    for _ in range(int(input())):
        n = input().strip().split("-")
        if n[0] not in d:
            d[n[0]]=[n[1]]
        else:
            d[n[0]]+=[n[1]]
    for i,j in d.items():
        print(i)
        for z in j:
            print(z)
main()
