"""Palindrome"""
def main():
    """Palindrome"""
    n = int(input())
    num = input()
    s=0
    i=0
    num1=""
    for i in num:
        if i.isnumeric():
            num1+=i
    num1 = int(num1)
    while s!=n:
        num1+=1
        if len(str(num1))>=3:
            if int(str(num1)[-3::-1][::-1])>23:
                num1=0
                print("0:00")
                s+=1
        if not num1%10 and 0<num1<60:
            print("0"+":"+str(num1))
            s+=1
        if len(str(num1))>=3:
            n3 = str(num1)[-3::-1][::-1]
            n4 = str(num1)[-1:-3:-1][::-1]
            if str(num1)[::-1] == str(num1) and int(str(num1)[-2:-3:-1])<6 \
            and int(str(num1)[-3::-1][::-1])<=24:
                s+=1
                print(n3+":"+n4)
main()
