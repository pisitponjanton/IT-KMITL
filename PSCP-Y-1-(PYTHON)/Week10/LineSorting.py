"""LineSorting"""
def main():
    """LineSorting"""
    n = int(input())
    t = []
    for _ in range(n):
        t.append(input())
    t.sort(key=len)
    for i in t:
        print(i)
main()
