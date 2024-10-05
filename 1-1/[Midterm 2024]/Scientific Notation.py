"""Scientific Notation"""
def numin1(num):
    """Scientific Notation"""
    n=0
    dd="."
    num1=""
    for i in num[::-1]:
        if i!="0" and not n:
            n=1
        if n:
            num1+=i
    num1=num1[::-1] if num1 else ""
    if len(num1)<=1:
        dd=""
    return dd,num1
def numin2(num):
    """Scientific Notation"""
    t=""
    n=0
    s=-1
    num1=""
    dd="."
    for i in num:
        if i==".":
            n=1
        if i!="." and not n:
            s+=1
        if i!=".":
            num1+=i
    if num1[0] == "0":
        s=1
        n=0
        t="-"
        for i in num1[1:]:
            if i=="0" and not n:
                s+=1
            else:
                n=1
        num1=num1[s:]
        if len(num1)<=1:
            dd=""
    return t,dd,num1,s
def numin3(num):
    """Scientific Notation"""
    num1=""
    num2=""
    n=0
    s=-1
    for i in num:
        if i.isspace():
            break
        if i == ".":
            n=1
        if n:
            s+=1
        if i!=".":
            num1+=i
    s=0 if s==-1 else s
    for i in num[::-1]:
        if i.isnumeric():
            num2+=i
        else:
            break
    return num1,num2,s
def numin4(num):
    """Scientific Notation"""
    num1=""
    num2=""
    for i in num:
        if i.isspace():
            break
        if i!=".":
            num1+=i
    for i in num[::-1]:
        if i.isnumeric():
            num2+=i
        else:
            break
    return num1,num2
def main():
    """Scientific Notation"""
    num = input()
    x=0
    dot=0
    de=""
    x=1 if "x" in num else 0
    dot=1 if "." in num else 0
    if not x:
        if float(num)<0:
            num=num[1:]
            de="-"
        if not dot:
            dd,num1 = numin1(num)
            print(f"{de}{num1[0]}{dd}{num1[1:]} x 10^{len(num)-1}" if num1 else "0")
        else:
            t,dd,num1,s = numin2(num)
            print(f"{de}{num1[0]}{dd}{num1[1:]} x 10^{t}{s}" if float(num) else "0")
    else:
        if num[0]=="-":
            de="-"
            num=num[1:]
        if not "-" in num:
            num1,num2,s = numin3(num)
            if s>int(num2[::-1]):
                print(de+num1[0:int(num[-1])+1]+"."+num1[int(num2[::-1])+1:])
            else:
                num1=num1+"0"*(int(num2[::-1])-s)
                print(de+num1)
        else:
            num1,num2 = numin4(num)
            print(de+"0."+("0"*(int(num2[::-1])-1))+num1)
main()
