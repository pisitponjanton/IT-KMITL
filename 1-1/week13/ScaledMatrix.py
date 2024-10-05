"""ScaledMatrix"""
def main(a,b):
    """ScaledMatrix"""
    n = [float(input()) for _ in range(a*b)]
    i=0
    for _ in range(a):
        for _ in range(b):
            print(f"{(n[i]-min(n))/(max(n)-min(n)):.2f}",end=" ")
            i+=1
        print()
main(int(input()),int(input()))
