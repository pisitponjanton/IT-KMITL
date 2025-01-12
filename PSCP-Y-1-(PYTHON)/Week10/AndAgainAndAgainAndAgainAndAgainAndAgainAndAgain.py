"""AndAgainAndAgainAndAgainAndAgainAndAgainAndAgain"""
def main():
    """AndAgainAndAgainAndAgainAndAgainAndAgainAndAgain"""
    num = input().replace(".","").split()
    k = []
    for i in num:
        s=0
        for j in i:
            if 'a' in j:
                s+=1
            elif 'e' in j:
                s+=1
            elif 'i' in j:
                s+=1
            elif 'o' in j:
                s+=1
            elif 'u' in j:
                s+=1
        if s>=2:
            k.append(i)
    if len(k)>=1:
        k.sort()
        for i in k:
            print(i)
    else:
        print("Nope")
main()
