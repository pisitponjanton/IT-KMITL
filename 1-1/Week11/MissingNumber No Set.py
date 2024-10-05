"""MissingNumber No Set"""
def main():
    """MissingNumber No Set"""
    n = int(input())
    nn=[]
    nnn=[]
    while True:
        num = int(input())
        if not num:
            break
        nn.append(num)
    for i in range(1,n+1):
        nnn.append(i)
    for i in nnn:
        if not i in nn:
            print(i)
main()
