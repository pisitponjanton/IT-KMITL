"""LastStand"""
def main():
    """LastStand"""
    n = input().replace("[","").replace("]","").replace(","," ").split()
    s=0
    for _ in n:
        print(n[s][-1])
        s+=1
main()
