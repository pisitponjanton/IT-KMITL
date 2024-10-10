"""ชีวะจักรโบราณ"""
def nine(n):
    """t+=l[i]"""
    n1=n//9
    n2="9"
    s=1
    while n1>=9:
        n1=n1//9
        n2+="x9"
        s+=1
    for i in range(1,9+1):
        if (9**s)*i > n or i==9:
            if i-1>1:
                n2+="x"+str(i-1)
            break
    return n2,s,i
def main(n):
    """ชีวะจักรโบราณ"""
    l = {"0":'zezeso',"1":'papan',"2":'dogugu',
        "3":'gushigi',"4":'zugogo',"5":'zugagi',
        "6":'gibugu',"7":'gezun',"8":'gegido',
        "9":'bagin',"+":"do","x":"gu"}
    n2=""
    if n<10:
        print(l[str(n)])
    else:
        n2,s,i=nine(n)
        n3=n-(9**s)*(i-1)
        while n3>10:
            n21,s,i=nine(n3)
            n3=n3-(9**s)*(i-1)
            n2+="+"+n21
        n2+="+"+str(n3) if n3>0 else ""
        t=""
        # print(n2)
        for i in n2:
            t+=l[i]
            if not i.isnumeric():
                t+=" "
        print(t)
main(int(input()))
