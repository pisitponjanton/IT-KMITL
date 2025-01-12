"""CaesarV2"""
def main():
    """CaesarV2"""
    l=["what", "when", "why", "which", "this", "there", "where",
       "the", "is", "am", "are", "you", "we", "they", "he", "she",
       "it"]
    t = input()
    s=""
    r=0
    for j in range(-26,27):
        for i in t:
            if i.isalpha():
                if i.islower():
                    y=ord(i)+j
                    y-=26 if y>122 else 0
                    y+=26 if y<97 else 0
                    s+=chr(y)
                else:
                    y=ord(i)+j
                    y-=26 if y>90 else 0
                    y+=26 if y<65 else 0
                    s+=chr(y)
            else:
                s+=i
        s=s.split()
        for i in s:
            if i in l:
                r=1
                break
        if not r:
            s=""
        else:
            break
    print(*s)
main()
