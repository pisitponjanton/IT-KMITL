"""PickThemAgain"""
def main(n):
    """PickThemAgain"""
    l = [i for i in n if not int(i)%3 or not int(i)%5]
    if l:
        for i in l[::-1]:
            print(i)
    else:
        print("Nope")
main(input().split())
