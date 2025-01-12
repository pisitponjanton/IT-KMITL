"""Music Lover"""
def main(n):
    """Music Lover"""
    d={}
    for _ in range(n):
        n=input().strip().split("-")
        if n[0] not in d:
            d[n[0]]=[n[1]]
        else:
            d[n[0]].append(n[1])
    for i,j in d.items():
        print(i)
        for z in j:
            print(z)
main(int(input()))
