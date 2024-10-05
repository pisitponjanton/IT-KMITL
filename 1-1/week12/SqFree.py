"""SqFree"""
def main():
    """SqFree"""
    n=0
    for i in range(1,int(input())+1):
        t=True
        for j in range(2,int(i**0.5)+1):
            if not i%(j**2):
                t=False
        if t:
            n+=1
    print(n)
main()
