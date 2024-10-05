"""PickThemAgain"""
def main():
    """PickThemAgain"""
    n = input().split()
    s=0
    for i in n[::-1]:
        if not int(i)%3 or not int(i)%5:
            print(i)
            s+=1
    if s<=0:
        print("Nope")
main()
