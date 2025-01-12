"""Matrix_MN"""
def main():
    """Matrix_MN"""
    n1 = int(input())
    n2 = int(input())
    l = []
    i=0
    for _ in range(n1*n2):
        l.append(int(input()))
    for _ in range(n1):
        for _ in range(n2):
            print(l[i],end=" ")
            i+=1
        print()
main()
