""" Number Message"""
def main():
    """ Number Message"""
    n = input()
    t=""
    s=0
    for i in n:
        if i == "1":
            if s<len(n):
                if n[s+1] == "2":
                    t+="R"
                elif n[s+1] == "3":
                    t+="B"
                else:
                    t+="I"
            else:
                t+="I"
        elif i == "3" and n[s-1]!="1":
            t+="E"
        elif i == "4":
            t+="A"
        elif i == "5":
            t+="S"
        elif i == "0":
            t+="O"
        elif not i.isnumeric():
            t+=i.upper()
        s+=1
    print(t)
main()
