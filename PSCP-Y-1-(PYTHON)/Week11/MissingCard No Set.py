"""MissingCard No Set"""
def main():
    """MissingCard No Set"""
    c = [
    "AS", "AH", "AD", "AC",
    "KS", "KH", "KD", "KC",
    "QS", "QH", "QD", "QC",
    "JS", "JH", "JD", "JC",
    "10S", "10H", "10D", "10C",
    "9S", "9H", "9D", "9C",
    "8S", "8H", "8D", "8C",
    "7S", "7H", "7D", "7C",
    "6S", "6H", "6D", "6C",
    "5S", "5H", "5D", "5C",
    "4S", "4H", "4D", "4C",
    "3S", "3H", "3D", "3C",
    "2S", "2H", "2D", "2C" ]
    c1=[]
    for _ in range(51):
        c1.append(input())
    for i in c:
        if not i in c1:
            print(i)
main()
