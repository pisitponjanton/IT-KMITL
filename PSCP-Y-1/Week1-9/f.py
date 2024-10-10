"""r"""
def inputnum():
    """r"""
    num1 = int(input())
    num3 = int(input())
    num2 = int(input())
    strnum1 = str(num1)
    strnum2 = str(num2)
    strnum3 = str(num3)
    return strnum1,strnum2,strnum3
def main():
    """r"""
    strnum1,strnum2,strnum3 = inputnum()
    t1 = len(strnum1)
    t2 = len(strnum2)
    t3 = len(strnum3)
    fnum1 = int(strnum1[0])
    fnum2 = int(strnum2[0])
    fnum3 = int(strnum3[0])
    if fnum1 != fnum2 != fnum3:
        fnum1 = int(strnum1[0])
        fnum2 = int(strnum2[0])
        fnum3 = int(strnum3[0])
    else:
        fnum1 = int(strnum1[t1-1])
        fnum2 = int(strnum2[t2-1])
        fnum3 = int(strnum3[t3-1])
        if fnum1 != fnum2 != fnum3:
            fnum1 = int(strnum1[t1-1])
            fnum2 = int(strnum2[t2-1])
            fnum3 = int(strnum3[t3-1])
        else:
            fnum1 = int(strnum1[t1-2])
            fnum2 = int(strnum2[t2-2])
            fnum3 = int(strnum3[t3-2])
            if fnum1 != fnum2 != fnum3:
                fnum1 = int(strnum1[t1-2])
                fnum2 = int(strnum2[t2-2])
                fnum3 = int(strnum3[t3-2])
            else:
                fnum1 = int(strnum1[t1-2])
                fnum2 = int(strnum2[t2-1])
                fnum3 = int(strnum3[t3-1])
    return fnum1,fnum2,fnum3,strnum1,strnum2,strnum3
def hlnum():
    """r"""
    fnum1,fnum2,fnum3,strnum1,strnum2,strnum3 = main()
    ans3 = 0
    ans1 = 0
    if fnum2 > ans3 :
        ans3 = fnum2
    if fnum3 > ans3 :
        ans3 = fnum3
    if fnum1 > ans3 :
        ans3 = fnum1
    if fnum1 > ans1 :
        ans1 = fnum1
    if fnum3 < ans1 :
        ans1 = fnum3
    if fnum2 < ans1 :
        ans1 = fnum2
    return fnum1,fnum2,fnum3,strnum1,strnum2,strnum3,ans3,ans1
def ifnum():
    """r"""
    fnum1,fnum2,fnum3,strnum1,strnum2,strnum3,ans3,ans1 = hlnum()
    ans2 = fnum1 + fnum2 + fnum3 - ans3 - ans1
    if ans1 == fnum1:
        ans1 = strnum1
    elif ans2 == fnum1:
        ans2 = strnum1
    elif ans3 == fnum1:
        ans3 = strnum1
    if ans1 == fnum2:
        ans1 = strnum2
    elif ans2 == fnum2:
        ans2 = strnum2
    elif ans3 == fnum2:
        ans3 = strnum2
    if ans1 == fnum3:
        ans1 = strnum3
    elif ans2 == fnum3:
        ans2 = strnum3
    elif ans3 == fnum3:
        ans3 = strnum3
    print(int(ans3+ans2+ans1))
ifnum()
