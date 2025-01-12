"""Facebook"""
def main():
    """Facebook"""
    d={}
    while True:
        num = input()
        if "?" in num:
            num=num.split(" ? ")
            if num[0] in d and num[1] in d:
                p = set(d[num[0]]).intersection(set(d[num[1]]))
            else:
                p = set()
            break
        num = num.split(" <-> ")
        if num[0] not in d:
            d[num[0]]=[num[1]]
        else:
            d[num[0]]+=[num[1]]
        if num[1] not in d:
            d[num[1]]=[num[0]]
        else:
            d[num[1]]+=[num[0]]
    if p:
        p=list(p)
        p.sort()
        for i in p:
            print(i)
    else:
        print("No mutual friend")
main()
