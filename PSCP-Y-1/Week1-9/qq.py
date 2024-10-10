"""Saint Seiya"""
def main():
    """Saint Seiya"""
    num = int(input())
    numf = int(input())
    n=0
    g=""
    for i in range(1,num+1):
        if n>=numf:
            g="f"
            break
        if g!="f":
            if not i%6:
                n+=1
            elif not i%2:
                n+=165
    print(n)
    num1 = (num-i)*12
    n+=num1
    print(n,i)
main()
