"""One For All"""
def main():
    """One For All"""
    num = int(input())
    tt = ''
    for i in range(1,num+1):
        t = input()
        if i == num:
            tt+=t+"_"+str(num)
            break
        if not i%2:
            tt+=t+("-"*i)
        else:
            tt+=t+("*"*i)
    print(tt)
main()
