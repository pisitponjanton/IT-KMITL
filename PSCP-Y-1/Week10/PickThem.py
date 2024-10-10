"""PickThem"""
def main():
    """PickThem"""
    n = input().replace("[","").replace("]","").replace(","," ").split()
    s=0
    for i in n:
        if not int(i)%2:
            print(i)
            s+=1
    if s<=0:
        print("Nope")
main()
