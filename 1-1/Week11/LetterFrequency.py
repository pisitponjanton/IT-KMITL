"""LetterFrequency"""
def main():
    """LetterFrequency"""
    n = input().lower()
    n1=""
    for i in n:
        if i.islower():
            n1+=i
    n1 = sorted(n1)
    n = []
    for i in n1:
        n.append([i,n1.count(i)])
    n.sort(key = lambda x: x[1])
    print(n[-1][0])
main()
